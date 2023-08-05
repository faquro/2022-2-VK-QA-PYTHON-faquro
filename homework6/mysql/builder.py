from .models import TotalRequestCount, RequestCountByType, Top_FrequentURL, Top_4XX_Error, Top_5XX_Error
from ..static import top, top_4XX, top_5XX

class MySQLBuilder:

    def __init__(self, client, path):
        self.client = client
        self.path = path
        self.requests = self.read_data()

    def read_data(self):
        with open(self.path) as file:
            requests = file.readlines()
            requests = [request.split() for request in requests]
            return requests

    def count_total(self):
        result = TotalRequestCount(count=sum(1 for _ in self.requests))
        self.client.session.add(result)
        self.client.session.commit()
        return result

    def count_by_type(self):
        temp_dict = {}
        for request in self.requests:
            request_type = request[5][1:]
            if request_type in temp_dict:
                temp_dict[request_type] += 1
            elif len(request_type) < 7:
                temp_dict[request_type] = 1

        result = []
        for request_type, count in temp_dict.items():
            row = RequestCountByType(count=int(count), type_name=request_type)
            result.append(row)
        self.client.session.bulk_save_objects(result)
        self.client.session.commit()
        return result

    def top(self):
        temp_dict = {}
        for request in self.requests:
            url = request[6]
            if url in temp_dict:
                temp_dict[url] += 1
            else:
                temp_dict[url] = 1

        result = []
        for url, count in sorted(temp_dict.items(), key=lambda x: x[1], reverse=True)[:top]:
            row = Top_FrequentURL(count=int(count), url=url)
            result.append(row)
        self.client.session.bulk_save_objects(result)
        self.client.session.commit()
        return result

    def top_4xx_requests(self):
        temp_data = []
        for request in self.requests:
            url = request[6]
            status = request[8]
            size = request[9]
            ip = request[0]
            if status[0] == '4':
                item = (url, status, int(size), ip)
                temp_data.append(item)

        result = []
        for item in sorted(temp_data, key=lambda x: x[2], reverse=True)[:top_4XX]:
            row = Top_4XX_Error(url=item[0], code=int(item[1]), size=int(item[2]), ip=item[3])
            result.append(row)
        self.client.session.bulk_save_objects(result)
        self.client.session.commit()
        return result

    def top_5xx_users(self):
        temp_dict = {}
        for request in self.requests:
            ip = request[0]
            status = request[8]
            if status[0] == '5':
                if ip in temp_dict:
                    temp_dict[ip] += 1
                else:
                    temp_dict[ip] = 1

        result = []
        for ip, count in sorted(temp_dict.items(), key=lambda x: x[1], reverse=True)[:top_5XX]:
            row = Top_5XX_Error(ip=ip, count=int(count))
            result.append(row)
        self.client.session.bulk_save_objects(result)
        self.client.session.commit()
        return result
