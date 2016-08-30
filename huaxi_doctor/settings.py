# -*- coding: utf-8 -*-
BOT_NAME = 'huaxi_doctor'

SPIDER_MODULES = ['huaxi_doctor.spiders']
NEWSPIDER_MODULE = 'huaxi_doctor.spiders'

ITEM_PIPELINES = {
    'huaxi_doctor.pipelines.HuaxiDoctorPipeline': 300,
}
USER_AGENT = ""
COOKIES_ENABLED = True

MONGODB_HOST = '127.0.0.1'
MONGODB_PORT = 27017
MONGODB_DBNAME = 'huaxiHospital'
MONGODB_DOCNAME = 'Doctor'

ROBOTSTXT_OBEY = True
