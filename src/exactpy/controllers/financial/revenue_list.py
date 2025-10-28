from exactpy.controllers.base import BaseController
from exactpy.models.financial import (
    RevenueListModel,
)


class RevenueListController(BaseController):
    _resource = "read/financial/RevenueList"
    _mandatory_query_arg_options = []
    _mandatory_filter_options = []
    _model = RevenueListModel


class RevenueListByYearController(BaseController):
    _resource = "read/financial/RevenueListByYear"
    _mandatory_query_arg_options = ["year"]
    _mandatory_filter_options = []
    _model = RevenueListModel


class RevenueListByYearAndStatusController(BaseController):
    _resource = "read/financial/RevenueListByYearAndStatus"
    _mandatory_query_arg_options = ["year", "afterEntry"]
    _mandatory_filter_options = []
    _model = RevenueListModel
