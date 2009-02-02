#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Adam Benzan (adam@saltminesoftware.com)"
__date__   = "Sat Jan 31 06:34:41 2009"

class Action:
    def __init__(self, actor):
        self.actor = actor

class WaitAction(Action):
    def execute(self, target=None):
        self.actor.hp += 1

class AttackAction(Action):
    def execute(self, target):
        target.hp -= 1
    
class MoveTowardAction(Action):
    def execute(self,target):
        self.actor
