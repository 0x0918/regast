from typing import Optional

from regast.core.expressions.expression import Expression

class SliceAccess(Expression):
    def __init__(
        self, 
        object: Expression,
        start: Optional[Expression] = None,
        stop: Optional[Expression] = None,
    ):
        super().__init__()

        self._object: Expression = object
        self._start: Optional[Expression] = start
        self._stop: Optional[Expression] = stop

    @property
    def object(self) -> Expression:
        return self._object
    
    @property
    def start(self) -> Optional[Expression]:
        return self._start

    @property
    def stop(self) -> Optional[Expression]:
        return self._stop

    @property
    def __str__(self):
        start = str(self.start) if self.start else ""
        stop = str(self.stop) if self.stop else ""
        return str(self.object) + "[" + start + ":" + stop + "]"
    
    @property
    def __eq__(self, other):
        if isinstance(other, SliceAccess):
            return self.object == other.object and self.start == other.start and self.stop == other.stop
        return False