import json

from sanic import Blueprint
from sanic import response

import akshare

stockApi = Blueprint("stockApi", url_prefix="/stock")


@stockApi.route("/")
async def bp_root(request):
    """
       沪深京 A 股列表
       :return: 沪深京 A 股数据
       :rtype: json([{code,name}])
    """
    pd = akshare.stock_info_a_code_name()
    ret = pd.to_json(orient='records')
    return response.json({"my": json.loads(ret)})
