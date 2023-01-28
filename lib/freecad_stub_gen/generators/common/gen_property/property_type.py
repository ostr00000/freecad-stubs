import enum


class PropertyType(enum.IntFlag):
    description: str

    def __new__(cls, value, description=None):
        member = int.__new__(cls, value)
        member._value_ = value

        if description is None:
            description = '\n'.join(flag.description for flag in member)
        member.description = description

        return member

    def __iter__(self):
        for e in type(self):
            if e.value & self.value:
                yield e

    Prop_None = 0, "No special property type"
    Prop_ReadOnly = 1, "Property is read-only in the editor"
    Prop_Transient = 2, "Property content won't be saved to file, " \
                        "but still saves name, type and status"
    Prop_Hidden = 4, "Property won't appear in the editor"
    Prop_Output = 8, "Modified property doesn't touch its parent container"
    Prop_NoRecompute = 16, "Modified property doesn't touch its container for recompute"
    Prop_NoPersist = 32, "Property won't be saved to file at all"
