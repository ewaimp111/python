#!/usr/bin/env python3

import codepage as cp  #测试代码模块类Car

car=cp.Car('德国','奥迪A6',2016)

car.show_info()
car.usetank()
l = car.read_odo()
print(l)

ecar = cp.Eleccar('法国','特斯拉',2011)
ecar.show_info();
ecar.usetank()


class AnonymousSurvey():
    def __init__(self,question):
        """存储一个问题，并为存储答案做准备"""
        self.question = question
        self.responses = []
    def show_question(self):
        print(question)
    def store_response(self, new_response):
        self.responses.append(new_response)
    def show_results(self):
        print("Survey results:")

        for response in self.responses:

            print('- ' + response)


question = "What language did you first learn to speak?"
my_survey = AnonymousSurvey(question)
#显示问题并存储答案 my_survey.show_question()
print("Enter 'q' at any time to quit.\n")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    my_survey.store_response(response)

print('\n Thank you to everyone who participated in the survey!')
my_survey.show_results()

