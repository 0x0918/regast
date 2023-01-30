from typing import List, Optional
from regast.core.core import Core

from regast.core.expressions.expression import Expression
from regast.core.expressions.identifier import Identifier
from regast.core.statements.statement import Statement
from regast.core.types.type import Type
from regast.core.variables.variable import DataLocation
from regast.parsing.ast_node import ASTNode

class VariableDeclaration(Core):
    def __init__(self, node: ASTNode):
        super().__init__(node)

        self._type: Type = None
        self._name: Identifier = None
        self._data_location: Optional[DataLocation] = None
        
    @property
    def type(self) -> Type:
        return self._type

    @property
    def name(self) -> Identifier:
        return self._name

    @property
    def data_location(self) -> Optional[DataLocation]:
        return self._data_location

    @property
    def children(self) -> List:
        children = [self.type, self.name]
        if self.data_location:
            children.append(self.data_location)
        return children

    def __eq__(self, other):
        if isinstance(other, VariableDeclaration):
            return (
                self.type == other.type and
                self.name == other.name and
                self.data_location == other.data_location 
            )
        return False
    
class VariableDeclarationStatement(Statement):
    def __init__(self, node: ASTNode):
        super().__init__(node)

        self._variable_declaration: VariableDeclaration = None
        self._expression: Optional[Expression] = None

    @property
    def variable_declaration(self) -> VariableDeclaration:
        return self._variable_declaration

    @property
    def type(self) -> Type:
        return self.variable_declaration.type

    @property
    def name(self) -> Identifier:
        return self.variable_declaration.name

    @property
    def data_location(self) -> Optional[DataLocation]:
        return self.variable_declaration.data_location

    @property
    def initial_expression(self) -> Optional[Expression]:
        return self._expression

    @property
    def children(self) -> List:
        if self.initial_expression:
            return [self.variable_declaration, self.initial_expression]
        return [self.variable_declaration]

    def __eq__(self, other):
        if isinstance(other, VariableDeclarationStatement):
            return (
                self.variable_declaration == other.variable_declaration and
                self.initial_expression == other.initial_expression
            )
        return False

class VariableDeclarationFromTupleStatement(Statement):
    def __init__(self, node: ASTNode):
        super().__init__(node)

        self._variable_declarations: List[VariableDeclaration] = []
        self._expression: Expression = None
        
    @property
    def variable_declarations(self) -> List[VariableDeclaration]:
        return list(self._variable_declarations)

    @property
    def initial_expression(self) -> Expression:
        return self._expression

    @property
    def children(self) -> List:
        return self.variable_declarations + [self.initial_expression]
        
    def __eq__(self, other):
        if isinstance(other, VariableDeclarationFromTupleStatement):
            return (
                self.variable_declarations == other.variable_declarations and
                self.initial_expression == other.initial_expression
            )
        return False

class VariableDeclarationWithVarStatement(Statement):
    def __init__(self, node: ASTNode):
        """
        Deprecated since v0.4.20
        var (x, y, z) = f()
        """
        super().__init__(node)

        self._names: List[Identifier] = []
        self._expression: Expression = None

    @property
    def names(self) -> List[Identifier]:
        return self._names

    @property
    def initial_expression(self) -> Expression:
        return self._expression

    @property
    def children(self) -> List:
        return self.names + [self.initial_expression]

    def __eq__(self, other):
        if isinstance(other, VariableDeclarationWithVarStatement):
            return self.names == other.names and self.initial_expression == other.initial_expression
        return False