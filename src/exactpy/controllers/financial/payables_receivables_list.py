from exactpy.controllers.base import BaseController
from exactpy.models.financial import PayablesReceivablesListModel


class PayablesListController(BaseController):
    _resource = "read/financial/PayablesList"
    _mandatory_query_arg_options = []
    _mandatory_filter_options = []
    _model = PayablesReceivablesListModel
    _expand = []


class ReceivablesListController(BaseController):
    _resource = "read/financial/ReceivablesList"
    _mandatory_query_arg_options = []
    _mandatory_filter_options = []
    _model = PayablesReceivablesListModel
    _expand = []


class PayablesListByAgeGroupController(BaseController):
    _resource = "read/financial/PayablesListByAgeGroup"
    _mandatory_query_arg_options = ["ageGroup"]
    _mandatory_filter_options = []
    _model = PayablesReceivablesListModel
    _expand = []


class ReceivablesListByAgeGroupController(BaseController):
    _resource = "read/financial/ReceivablesListByAgeGroup"
    _mandatory_query_arg_options = ["ageGroup"]
    _mandatory_filter_options = []
    _model = PayablesReceivablesListModel
    _expand = []


class PayablesListByAccountController(BaseController):
    _resource = "read/financial/PayablesListByAccount"
    _mandatory_query_arg_options = ["accountId"]
    _mandatory_filter_options = []
    _model = PayablesReceivablesListModel
    _expand = []


class ReceivablesListByAccountController(BaseController):
    _resource = "read/financial/ReceivablesListByAccount"
    _mandatory_query_arg_options = ["accountId"]
    _mandatory_filter_options = []
    _model = PayablesReceivablesListModel
    _expand = []


class PayablesListByAccountAndAgeGroupController(BaseController):
    _resource = "read/financial/PayablesListByAccountAndAgeGroup"
    _mandatory_query_arg_options = ["accountId", "ageGroup"]
    _mandatory_filter_options = []
    _model = PayablesReceivablesListModel
    _expand = []


class ReceivablesListByAccountAndAgeGroupController(BaseController):
    _resource = "read/financial/ReceivablesListByAccountAndAgeGroup"
    _mandatory_query_arg_options = ["accountId", "ageGroup"]
    _mandatory_filter_options = []
    _model = PayablesReceivablesListModel
    _expand = []
