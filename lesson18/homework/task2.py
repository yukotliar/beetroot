# Implement 2 classes, the first one is the Boss and the second one is the Worker.
#
# Worker has a property 'boss', and its value must be an instance of Boss.
#
# You can reassign this value, but you should check whether the new value is Boss. Each Boss has a list of his own workers.
# You should implement a method that allows you to add workers to a Boss.
# You're not allowed to add instances of Boss class to workers list directly via access to attribute, use getters and setters instead!

class Boss:
    def __init__(self, name):
        self.name = name
        self.workers = []

    @property
    def my_workers(self):
        print('get my workers')
        return self.workers

    @my_workers.setter
    def my_workers(self, worker):
        print('set my workers')
        worker.boss.workers.remove(worker.name)
        self.workers.append(worker.name)


class Worker:
    def __init__(self, name, boss):
        self.name = name
        self.boss = boss
        self.boss.workers.append(self.name)

    @property
    def my_boss(self):
        print('get my boss')
        return self.boss

    @my_boss.setter
    def my_boss(self, new_boss):
        print('set my boss')
        if not isinstance(new_boss, Boss):
            raise ValueError('it should be a boss')
        self.boss.workers.remove(self.name)
        self.boss = new_boss
        self.boss.workers.append(self.name)

boss1 = Boss('Jake')
boss2 = Boss('Gyll')
worker1 = Worker('Bob', boss1)
worker2 = Worker('Dylan', boss2)
worker1.my_boss = boss2
boss1.my_workers = worker1
print(boss1.workers)
print(boss2.workers)
