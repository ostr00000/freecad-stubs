from functools import cached_property

from freecad_stub_gen.generators.common.names import getModuleName
from freecad_stub_gen.util import OrderedSet, indent


class EmptyType:
    @property
    def value(self):
        return self

    def __eq__(self, other):
        return other is None or other == 'object'

    def __hash__(self):
        return 1

    def __str__(self):
        return 'object'


Empty = EmptyType()


class ArgumentsIter:
    @cached_property
    def imports(self):
        return OrderedSet()

    def __iter__(self):
        """
        Cannot inherit this class from Iterable/Iterator
        because super() will not find correct class.
        """
        for argType in super().__iter__():
            match argType:
                case str() if '[' not in argType and (mod := getModuleName(argType)):
                    self.imports.add(mod)
                case UnionArguments() as ua:
                    self.imports.update(ua.imports)
            yield str(argType)


class UnionArguments(ArgumentsIter, OrderedSet):
    def __str__(self):
        return ' | '.join(self)


class TupleArgument(ArgumentsIter, list):
    def __str__(self):
        if self:
            return f'tuple[{", ".join(self)}]'
        return 'tuple'


RetType = UnionArguments[str] | EmptyType | str


class InvalidReturnType(ValueError):
    pass


class DictArgument(ArgumentsIter):
    def __init__(self, literalKeys=False):
        self.literalKeys = literalKeys
        self.keys = UnionArguments()
        self.values = UnionArguments()

    def add(self, key: RetType, value: RetType):
        self.keys.add(key)
        self.values.add(value)

    def __bool__(self):
        return bool(self.keys and self.values)

    def __str__(self):
        if not self:
            return 'dict'

        if self.literalKeys:
            self.imports.add('typing')
            ret = f'dict[typing.Literal[{self.keys}], {self.values}]'
        else:
            ret = f'dict[{self.keys}, {self.values}]'

        self.imports.update(self.keys.imports)
        self.imports.update(self.values.imports)
        return ret


class TypedDictGen(DictArgument):
    def __init__(self, funName: str):
        super().__init__()
        self.funName = funName

    def __str__(self):
        lines = [f'{k}: {v}' for k, v in zip(self.keys, self.values)]
        content = indent('\n'.join(lines))
        typedDictName = f'Return{self.funName.capitalize()}Dict'
        fun = f"class {typedDictName}(typing.TypedDict):\n{content}"

        self.imports.add('typing')
        self.imports.update(self.keys.imports)
        self.imports.update(self.values.imports)
        self.imports.add(fun)
        return typedDictName
