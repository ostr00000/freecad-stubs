import pytest

from conftest import InputCode
from stub_gen.scan.filter_gen import genFunctions
from stub_gen.scan.function import genFunctionReturnValues


@pytest.mark.parametrize(
    'inputCode,',
    [
        InputCode(
            """
class A;
class B{
    boolean check(int x);
}
"""
        )
    ],
)
def test_no_return(inputCode: InputCode):
    assert list(genFunctions(inputCode.trWrapper.getChildren())) == []


@pytest.mark.parametrize(
    'inputCode',
    [
        InputCode(
            """
int simpleRet(int x) {
  int result = (x / 42);
  return result;
}

int fac(int n) {
    return (n>1) ? n*fac(n-1) : 1;
}

int withLambda(){
    auto lambdaFun = [](int x) { 
        return x * 2; 
    };
    return lambdaFun(42);
}
""",
            returnCount=1,
        )
    ],
)
def test_simple(inputCode: InputCode):
    for c in genFunctions(inputCode.trWrapper.getChildren()):
        returnValues = list(genFunctionReturnValues(c))
        assert len(returnValues) == inputCode.returnCount


@pytest.mark.parametrize(
    'inputCode',
    [
        InputCode(
            """
int simpleRet(int x) {
    if (x % 2 == 0) {
        return x / 2;
    }else{ 
        return 3 * x;
    }
}
""",
            returnCount=2,
        ),
        InputCode(
            """
int withLambda(int y){
    auto lambdaFun = [](int x) {
        if (x % 2 == 0) {
            return x / 2;
        }else{ 
            return 3 * x;
        } 
    };
    if (y % 2 == 0) {
        return lambdaFun(y / 2);
    }else{ 
        return lambdaFun(y);
    }
}
""",
            returnCount=2,
        ),
    ],
)
def test_branches(inputCode: InputCode):
    for c in genFunctions(inputCode.trWrapper.getChildren()):
        returnValues = list(genFunctionReturnValues(c))
        assert len(returnValues) == inputCode.returnCount
