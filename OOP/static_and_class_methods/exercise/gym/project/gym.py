from project.customer import Customer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.subscription import Subscription
from project.trainer import Trainer


class Gym:
    def __init__(self):
        self.customers: list[Customer] = []
        self.trainers: list[Trainer] = []
        self.equipment: list[Equipment] = []
        self.plans: list[ExercisePlan] = []
        self.subscriptions: list[Subscription] = []


    @staticmethod
    def __add_objects(curr_object, object_collection):
        if curr_object not in object_collection:
            object_collection.append(curr_object)

    def add_customer(self, customer: Customer) -> None:
       self.__add_objects(customer, self.customers)

    def add_trainer(self, trainer: Trainer):
        self.__add_objects(trainer, self.trainers)

    def add_equipment(self, equipment: Equipment):
        self.__add_objects(equipment, self.equipment)

    def add_plan(self, plan: ExercisePlan):
        self.__add_objects(plan, self.plans)

    def add_subscription(self, subscription: Subscription):
        self.__add_objects(subscription, self.subscriptions)

    def subscription_info(self, subscription_id: int):
