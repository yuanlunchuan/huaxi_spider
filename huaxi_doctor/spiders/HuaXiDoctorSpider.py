import scrapy

class HuaXiDoctorSpider(scrapy.Spider):
  name = 'huaxi_doctor_spider'
  allowed_domains = ['www.cd120.com']
  # http: // www.cd120.com / findDoctorListByRegService.jspx?pageNo = 2 & regCode = 33
  start_urls = [ ]
  for i in [1, 2, 3, 4, 5]:
    new_url = "http://www.cd120.com/findDoctorListByRegService.jspx?pageNo="+str(i)+"&regCode=33"
    start_urls.append(new_url)
  for url in start_urls:
    print("----------start_urls: "+url)

  def parse(self, response):
    filename = 'huaxi_doctors'
    with open(filename, 'wb') as f:
      doctors = response.xpath("//tr[@id='ret']")
      for doctor in doctors:
        f = open('huaxi_doctor_result.txt', 'a', encoding='utf-8')
        f.writelines("医生名字: " + doctor.xpath("td[2]/span/a/i/text()").extract()[0])
        f.writelines("    " + doctor.xpath("td[3]/span/text()").extract()[0])
        f.writelines("    " + doctor.xpath("td[4]/span/em/text()").extract()[0] + "\n")
      f.close()
