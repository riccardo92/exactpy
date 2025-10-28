from exactpy.controllers.base import BaseController
from exactpy.models.financial import AgingPayablesReceivablesListModel


class AgingPayablesListController(BaseController):
    _resource = "read/financial/AgingPayablesList"
    _mandatory_query_arg_options = []
    _mandatory_filter_options = []
    _model = AgingPayablesReceivablesListModel
    _expand = []


class AgingReceivablesListController(BaseController):
    _resource = "read/financial/AgingReceivablesList"
    _mandatory_query_arg_options = []
    _mandatory_filter_options = []
    _model = AgingPayablesReceivablesListModel
    _expand = []


class AgingPayablesListByAgeGroupController(BaseController):
    _resource = "read/financial/AgingPayablesListByAgeGroup"
    _mandatory_query_arg_options = ["ageGroup"]
    _mandatory_filter_options = []
    _model = AgingPayablesReceivablesListModel
    _expand = []


class AgingReceivablesListByAgeGroupController(BaseController):
    _resource = "read/financial/AgingReceivablesListByAgeGroup"
    _mandatory_query_arg_options = ["ageGroup"]
    _mandatory_filter_options = []
    _model = AgingPayablesReceivablesListModel
    _expand = []
