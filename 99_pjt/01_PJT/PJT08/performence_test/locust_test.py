from locust import HttpUser, task, between

class SampleUser(HttpUser):
    wait_time = between(1, 3)

    def on_start(self):
        print('test start')


    # 해당주소에 get요청을 보낼거야 란 뜻.
    @task
    def normal_sort(self):
        # http://localhost:8089/가 앞에 붙는다
        self.client.get("test/normal_sort/")




    # @task
    # def priority_queue(self):
    #     self.client.get("test/priority_queue/")

    # @task
    # def bubble_sort(self):
    #     self.client.get("test/bubble_sort/")


