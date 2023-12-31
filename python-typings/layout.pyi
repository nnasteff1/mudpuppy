from _typeshed import Incomplete
from mudpuppy_core import BufferConfig as BufferConfig, BufferId as BufferId, Constraint as Constraint, Direction, Event as Event, LayoutNode, SessionId as SessionId, SessionInfo
from typing import Any, Awaitable, Callable

LayoutHandler = Callable[[SessionInfo, Any], Awaitable[None]]

class LayoutManager:
    callbacks: list[LayoutHandler]
    layouts: dict[SessionId, LayoutNode]
    def __init__(self) -> None: ...
    def add_callback(self, callback: LayoutHandler): ...
    def remove_callback(self, callback: LayoutHandler): ...
    async def on_new_session(self, sesh_info: SessionInfo): ...
    def get_constraint(self, sesh_id: SessionId, section_name: str) -> Constraint: ...
    def hide_section(self, sesh_id: SessionId, section_name: str): ...
    def show_section(self, sesh_id: SessionId, section_name: str, constraint: Constraint): ...
    async def extend_section(self, sesh_id: SessionId, *, section_name: str, new_section_name: str, constraint: Constraint, direction: Direction = ..., margin: int = 0, buffer_config: BufferConfig = None) -> BufferId | None: ...
    async def split_section(self, sesh_id: SessionId, *, section_name: str, constraint: Constraint, old_section_first: bool = True, new_section_name: str, new_constraint: Constraint, direction: Direction = ..., margin: int = 0, buffer_config: BufferConfig = None): ...

async def setup_session(event: Event): ...
async def on_resume(event: Event): ...

manager: Incomplete
