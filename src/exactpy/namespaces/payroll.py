from __future__ import annotations

from typing import TYPE_CHECKING

from exactpy.controllers.payroll import ActiveEmploymentController
from exactpy.namespaces.base import Namespace

if TYPE_CHECKING:
    from exactpy.client import Client


class PayrollNamespace(Namespace):
    active_employments: ActiveEmploymentController

    def __init__(self, client: Client):
        super().__init__(client=client)

        self.active_employments = ActiveEmploymentController(self._client)
