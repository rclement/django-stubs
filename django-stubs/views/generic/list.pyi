from typing import Any, Dict, Optional, Sequence, Tuple, Type

from django.core.paginator import Paginator
from django.db.models.query import QuerySet
from django.views.generic.base import ContextMixin, TemplateResponseMixin, View

from django.db.models import Model
from django.http import HttpRequest, HttpResponse

class MultipleObjectMixin(ContextMixin):
    allow_empty: bool = ...
    queryset: Optional[QuerySet] = ...
    model: Optional[Type[Model]] = ...
    paginate_by: Optional[int] = ...
    paginate_orphans: int = ...
    context_object_name: Optional[str] = ...
    paginator_class: Type[Paginator] = ...
    page_kwarg: str = ...
    ordering: Sequence[str] = ...
    request: HttpRequest = ...
    kwargs: Dict[str, Any] = ...
    object_list: QuerySet = ...
    def get_queryset(self) -> QuerySet: ...
    def get_ordering(self) -> Sequence[str]: ...
    def paginate_queryset(self, queryset: QuerySet, page_size: int) -> Tuple[Paginator, int, QuerySet, bool]: ...
    def get_paginate_by(self, queryset: QuerySet) -> Optional[int]: ...
    def get_paginator(
        self, queryset: QuerySet, per_page: int, orphans: int = ..., allow_empty_first_page: bool = ..., **kwargs: Any
    ) -> Paginator: ...
    def get_paginate_orphans(self) -> int: ...
    def get_allow_empty(self) -> bool: ...
    def get_context_object_name(self, object_list: QuerySet) -> Optional[str]: ...

class BaseListView(MultipleObjectMixin, View):
    def render_to_response(self, context: Dict[str, Any], **response_kwargs: Any) -> HttpResponse: ...
    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse: ...

class MultipleObjectTemplateResponseMixin(TemplateResponseMixin):
    template_name_suffix: str = ...
    object_list: QuerySet = ...

class ListView(MultipleObjectTemplateResponseMixin, BaseListView): ...
