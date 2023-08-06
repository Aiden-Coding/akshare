
from datetime import datetime
import json

from sanic import Blueprint
from sanic import response

import akshare

stockApi = Blueprint("stockApi", url_prefix="/stock")


@stockApi.route("/stock_info_a_code_name")
async def stock_info_a_code_name(request):
    """
       沪深京 A 股列表
       :return: 沪深京 A 股数据
       :rtype: json([{code,name}])
    """
    pd = akshare.stock_info_a_code_name()
    ret = pd.to_json(orient='records')
    return response.json({"code": "0000", "data": json.loads(ret)})


@stockApi.route("/stock_zh_a_hist/<ticker>/range/<multiplier>/<timespan>/<from_time>/<to>")
async def stock_zh_a_hist(request, ticker, multiplier, timespan, from_time, to):
    """
    东方财富网-行情首页-沪深京 A 股-每日行情
    https://quote.eastmoney.com/concept/sh603777.html?from=classic
    :param symbol: 股票代码
    :type symbol: str
    :param period: choice of {'daily', 'weekly', 'monthly'}
    :type period: str
    :param start_date: 开始日期
    :type start_date: str
    :param end_date: 结束日期
    :type end_date: str
    :param adjust: choice of {"qfq": "前复权", "hfq": "后复权", "": "不复权"}
    :type adjust: str
    :param timeout: choice of None or a positive float number
    :type timeout: float
    :return: 每日行情
    :rtype: pandas.DataFrame
    """
    if timespan == 'day':
        # '1644289200000'
        from_time = datetime.fromtimestamp(int(from_time) / 1000).strftime('%Y%m%d')
        to = datetime.fromtimestamp(int(to) / 1000).strftime('%Y%m%d')
        timespan = 'daily'
    elif timespan == 'week':
        timespan = 'weekly'
        from_time = datetime.fromtimestamp(int(from_time) / 1000).strftime('%Y%m%d')
        to = datetime.fromtimestamp(int(to) / 1000).strftime('%Y%m%d')
    elif timespan == 'month':
        timespan = 'monthly'
        from_time = datetime.fromtimestamp(int(from_time) / 1000).strftime('%Y%m%d')
        to = datetime.fromtimestamp(int(to) / 1000).strftime('%Y%m%d')
    pd = akshare.stock_zh_a_hist(ticker, timespan, from_time, to)
    ret = pd.to_json(orient='records')
    return response.json({"code": "0000", "data": json.loads(ret)})
