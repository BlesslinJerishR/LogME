import requests
from lxml import html
import threading

# Duplicates Remover
# https://dedupelist.com/
urlsList = [
    'http://www.brainyquote.com/topics/change-quotes',
    'http://www.brainyquote.com/topics/knowledge-quotes',
    'http://www.brainyquote.com/topics/technology-quotes_8',
    'http://www.brainyquote.com/topics/inspirational-quotes',
    'http://www.brainyquote.com/topics/marriage-quotes_8',
    'http://www.brainyquote.com/topics/famous-quotes_8',
    'http://www.brainyquote.com/topics/success-quotes',
    'http://www.brainyquote.com/topics/famous-quotes_1',
    'http://www.brainyquote.com/topics/motivational-quotes_8',
    'http://www.brainyquote.com/topics/technology-quotes_1',
    'http://www.brainyquote.com/topics/motivational-quotes_1',
    'http://www.brainyquote.com/topics/chance-quotes',
    'http://www.brainyquote.com/topics/marriage-quotes_1',
    'http://www.brainyquote.com/topics/technology-quotes_9',
    'http://www.brainyquote.com/topics/life-quotes',
    'http://www.brainyquote.com/topics/leadership-quotes',
    'http://www.brainyquote.com/topics/marriage-quotes_9',
    'http://www.brainyquote.com/topics/teacher-quotes',
    'http://www.brainyquote.com/topics/famous-quotes_9',
    'http://www.brainyquote.com/topics/intelligence-quotes',
    'http://www.brainyquote.com/topics/technology-quotes_10',
    'http://www.brainyquote.com/topics/marriage-quotes_10',
    'http://www.brainyquote.com/topics/money-quotes',
    'http://www.brainyquote.com/topics/alone-quotes',
    'http://www.brainyquote.com/topics/famous-quotes_10',
    'http://www.brainyquote.com/topics/motivational-quotes_9',
    'http://www.brainyquote.com/topics/motivational-quotes_2',
    'http://www.brainyquote.com/topics/marriage-quotes_2',
    'http://www.brainyquote.com/topics/famous-quotes_2',
    'http://www.brainyquote.com/topics/technology-quotes_2',
    'http://www.brainyquote.com/topics/imagination-quotes',
    'http://www.brainyquote.com/topics/famous-quotes_11',
    'http://www.brainyquote.com/topics/positive-quotes',
    'http://www.brainyquote.com/topics/technology-quotes_11',
    'http://www.brainyquote.com/topics/moving-on-quotes',
    'http://www.brainyquote.com/topics/marriage-quotes_11',
    'http://www.brainyquote.com/topics/marriage-quotes_3',
    'http://www.brainyquote.com/topics/motivational-quotes_3',
    'http://www.brainyquote.com/topics/famous-quotes_3',
    'http://www.brainyquote.com/topics/technology-quotes_3',
    'http://www.brainyquote.com/topics/motivational-quotes_10',
    'http://www.brainyquote.com/topics/dreams-quotes',
    'http://www.brainyquote.com/topics/humor-quotes',
    'http://www.brainyquote.com/topics/famous-quotes_12',
    'http://www.brainyquote.com/topics/technology-quotes_12',
    'http://www.brainyquote.com/topics/positive-quotes',
    'http://www.brainyquote.com/topics/marriage-quotes_12',
    'http://www.brainyquote.com/topics/motivational-quotes_4',
    'http://www.brainyquote.com/topics/marriage-quotes_4',
    'http://www.brainyquote.com/topics/famous-quotes_4',
    'http://www.brainyquote.com/topics/technology-quotes_4',
    'http://www.brainyquote.com/topics/smile-quotes',
    'http://www.brainyquote.com/topics/hope-quotes',
    'http://www.brainyquote.com/topics/work-quotes',
    'http://www.brainyquote.com/topics/marriage-quotes_13',
    'http://www.brainyquote.com/topics/technology-quotes_13',
    'http://www.brainyquote.com/topics/famous-quotes_13',
    'http://www.brainyquote.com/topics/motivational-quotes_5',
    'http://www.brainyquote.com/topics/marriage-quotes_5',
    'http://www.brainyquote.com/topics/motivational-quotes_11',
    'http://www.brainyquote.com/topics/famous-quotes_5',
    'http://www.brainyquote.com/topics/technology-quotes_5',
    'http://www.brainyquote.com/topics/truth-quotes',
    'http://www.brainyquote.com/topics/god-quotes',
    'http://www.brainyquote.com/topics/marriage-quotes_14',
    'http://www.brainyquote.com/topics/famous-quotes_14',
    'http://www.brainyquote.com/topics/motivational-quotes_6',
    'http://www.brainyquote.com/topics/technology-quotes_6',
    'http://www.brainyquote.com/topics/technology-quotes_14',
    'http://www.brainyquote.com/topics/famous-quotes_6',
    'http://www.brainyquote.com/topics/experience-quotes',
    'http://www.brainyquote.com/topics/motivational-quotes_12',
    'http://www.brainyquote.com/topics/knowledge-quotes_7',
    'http://www.brainyquote.com/topics/change-quotes_7',
    'http://www.brainyquote.com/topics/marriage-quotes_6',
    'http://www.brainyquote.com/topics/travel-quotes',
    'http://www.brainyquote.com/topics/future-quotes',
    'http://www.brainyquote.com/topics/success-quotes_0',
    'http://www.brainyquote.com/topics/success-quotes_7',
    'http://www.brainyquote.com/topics/change-quotes_0',
    'http://www.brainyquote.com/topics/failure-quotes',
    'http://www.brainyquote.com/topics/knowledge-quotes_8',
    'http://www.brainyquote.com/topics/knowledge-quotes_0',
    'http://www.brainyquote.com/topics/change-quotes_8',
    'http://www.brainyquote.com/topics/time-quotes',
    'http://www.brainyquote.com/topics/inspirational-quotes_0',
    'http://www.brainyquote.com/topics/love-quotes',
    'http://www.brainyquote.com/topics/faith-quotes',
    'http://www.brainyquote.com/topics/success-quotes_8',
    'http://www.brainyquote.com/topics/knowledge-quotes_9',
    'http://www.brainyquote.com/topics/motivational-quotes_13',
    'http://www.brainyquote.com/topics/change-quotes_9',
    'http://www.brainyquote.com/topics/success-quotes_1',
    'http://www.brainyquote.com/topics/change-quotes_1',
    'http://www.brainyquote.com/topics/success-quotes_9',
    'http://www.brainyquote.com/topics/knowledge-quotes_10',
    'http://www.brainyquote.com/topics/knowledge-quotes_1',
    'http://www.brainyquote.com/topics/change-quotes_10',
    'http://www.brainyquote.com/topics/inspirational-quotes_1',
    'http://www.brainyquote.com/topics/success-quotes_10',
    'http://www.brainyquote.com/topics/knowledge-quotes_11',
    'http://www.brainyquote.com/topics/change-quotes_11',
    'http://www.brainyquote.com/topics/motivational-quotes_14',
    'http://www.brainyquote.com/topics/success-quotes_2',
    'http://www.brainyquote.com/topics/change-quotes_2',
    'http://www.brainyquote.com/topics/success-quotes_11',
    'http://www.brainyquote.com/topics/knowledge-quotes_12',
    'http://www.brainyquote.com/topics/knowledge-quotes_2',
    'http://www.brainyquote.com/topics/change-quotes_12',
    'http://www.brainyquote.com/topics/success-quotes_3',
    'http://www.brainyquote.com/topics/inspirational-quotes_2',
    'http://www.brainyquote.com/topics/change-quotes_3',
    'http://www.brainyquote.com/topics/success-quotes_12',
    'http://www.brainyquote.com/topics/knowledge-quotes_13',
    'http://www.brainyquote.com/topics/knowledge-quotes_3',
    'http://www.brainyquote.com/topics/change-quotes_13',
    'http://www.brainyquote.com/topics/inspirational-quotes_7',
    'http://www.brainyquote.com/topics/success-quotes_4',
    'http://www.brainyquote.com/topics/inspirational-quotes_3',
    'http://www.brainyquote.com/topics/change-quotes_4',
    'http://www.brainyquote.com/topics/success-quotes_13',
    'http://www.brainyquote.com/topics/knowledge-quotes_14',
    'http://www.brainyquote.com/topics/knowledge-quotes_4',
    'http://www.brainyquote.com/topics/change-quotes_14',
    'http://www.brainyquote.com/topics/success-quotes_5',
    'http://www.brainyquote.com/topics/inspirational-quotes_8',
    'http://www.brainyquote.com/topics/change-quotes_5',
    'http://www.brainyquote.com/topics/inspirational-quotes_4',
    'http://www.brainyquote.com/topics/success-quotes_14',
    'http://www.brainyquote.com/topics/leadership-quotes_7',
    'http://www.brainyquote.com/topics/knowledge-quotes_5',
    'http://www.brainyquote.com/topics/chance-quotes_7',
    'http://www.brainyquote.com/topics/success-quotes_6',
    'http://www.brainyquote.com/topics/inspirational-quotes_9',
    'http://www.brainyquote.com/topics/change-quotes_6',
    'http://www.brainyquote.com/topics/inspirational-quotes_5',
    'http://www.brainyquote.com/topics/teacher-quotes_7',
    'http://www.brainyquote.com/topics/leadership-quotes_8',
    'http://www.brainyquote.com/topics/knowledge-quotes_6',
    'http://www.brainyquote.com/topics/chance-quotes_8',
    'http://www.brainyquote.com/topics/teacher-quotes_0',
    'http://www.brainyquote.com/topics/chance-quotes_0',
    'http://www.brainyquote.com/topics/inspirational-quotes_6',
    'http://www.brainyquote.com/topics/teacher-quotes_8',
    'http://www.brainyquote.com/topics/leadership-quotes_9',
    'http://www.brainyquote.com/topics/inspirational-quotes_10',
    'http://www.brainyquote.com/topics/leadership-quotes_0',
    'http://www.brainyquote.com/topics/chance-quotes_9',
    'http://www.brainyquote.com/topics/life-quotes_0',
    'http://www.brainyquote.com/topics/teacher-quotes_9',
    'http://www.brainyquote.com/topics/leadership-quotes_10',
    'http://www.brainyquote.com/topics/chance-quotes_10',
    'http://www.brainyquote.com/topics/teacher-quotes_1',
    'http://www.brainyquote.com/topics/chance-quotes_1',
    'http://www.brainyquote.com/topics/teacher-quotes_10',
    'http://www.brainyquote.com/topics/leadership-quotes_11',
    'http://www.brainyquote.com/topics/inspirational-quotes_11',
    'http://www.brainyquote.com/topics/leadership-quotes_1',
    'http://www.brainyquote.com/topics/chance-quotes_11',
    'http://www.brainyquote.com/topics/life-quotes_1',
    'http://www.brainyquote.com/topics/teacher-quotes_11',
    'http://www.brainyquote.com/topics/leadership-quotes_12',
    'http://www.brainyquote.com/topics/chance-quotes_12',
    'http://www.brainyquote.com/topics/teacher-quotes_2',
    'http://www.brainyquote.com/topics/chance-quotes_2',
    'http://www.brainyquote.com/topics/inspirational-quotes_12',
    'http://www.brainyquote.com/topics/teacher-quotes_12',
    'http://www.brainyquote.com/topics/leadership-quotes_2',
    'http://www.brainyquote.com/topics/leadership-quotes_13',
    'http://www.brainyquote.com/topics/chance-quotes_13',
    'http://www.brainyquote.com/topics/life-quotes_2',
    'http://www.brainyquote.com/topics/teacher-quotes_3',
    'http://www.brainyquote.com/topics/chance-quotes_3',
    'http://www.brainyquote.com/topics/teacher-quotes_13',
    'http://www.brainyquote.com/topics/leadership-quotes_3',
    'http://www.brainyquote.com/topics/leadership-quotes_14',
    'http://www.brainyquote.com/topics/life-quotes_3',
    'http://www.brainyquote.com/topics/chance-quotes_14',
    'http://www.brainyquote.com/topics/inspirational-quotes_13',
    'http://www.brainyquote.com/topics/teacher-quotes_4',
    'http://www.brainyquote.com/topics/chance-quotes_4',
    'http://www.brainyquote.com/topics/teacher-quotes_14',
    'http://www.brainyquote.com/topics/money-quotes_7',
    'http://www.brainyquote.com/topics/life-quotes_4',
    'http://www.brainyquote.com/topics/leadership-quotes_4',
    'http://www.brainyquote.com/topics/intelligence-quotes_7',
    'http://www.brainyquote.com/topics/teacher-quotes_5',
    'http://www.brainyquote.com/topics/chance-quotes_5',
    'http://www.brainyquote.com/topics/inspirational-quotes_14',
    'http://www.brainyquote.com/topics/money-quotes_8',
    'http://www.brainyquote.com/topics/intelligence-quotes_8',
    'http://www.brainyquote.com/topics/life-quotes_5',
    'http://www.brainyquote.com/topics/teacher-quotes_6',
    'http://www.brainyquote.com/topics/chance-quotes_6',
    'http://www.brainyquote.com/topics/leadership-quotes_5',
    'http://www.brainyquote.com/topics/money-quotes_9',
    'http://www.brainyquote.com/topics/life-quotes_6',
    'http://www.brainyquote.com/topics/intelligence-quotes_9',
    'http://www.brainyquote.com/topics/intelligence-quotes_0',
    'http://www.brainyquote.com/topics/leadership-quotes_6',
    'http://www.brainyquote.com/topics/life-quotes_7',
    'http://www.brainyquote.com/topics/money-quotes_10',
    'http://www.brainyquote.com/topics/alone-quotes_0',
    'http://www.brainyquote.com/topics/intelligence-quotes_10',
    'http://www.brainyquote.com/topics/money-quotes_0',
    'http://www.brainyquote.com/topics/life-quotes_8',
    'http://www.brainyquote.com/topics/money-quotes_11',
    'http://www.brainyquote.com/topics/intelligence-quotes_11',
    'http://www.brainyquote.com/topics/intelligence-quotes_1',
    'http://www.brainyquote.com/topics/life-quotes_9',
    'http://www.brainyquote.com/topics/money-quotes_12',
    'http://www.brainyquote.com/topics/intelligence-quotes_12',
    'http://www.brainyquote.com/topics/alone-quotes_1',
    'http://www.brainyquote.com/topics/money-quotes_1',
    'http://www.brainyquote.com/topics/life-quotes_10',
    'http://www.brainyquote.com/topics/money-quotes_13',
    'http://www.brainyquote.com/topics/intelligence-quotes_13',
    'http://www.brainyquote.com/topics/intelligence-quotes_2',
    'http://www.brainyquote.com/topics/life-quotes_11',
    'http://www.brainyquote.com/topics/money-quotes_14',
    'http://www.brainyquote.com/topics/intelligence-quotes_14',
    'http://www.brainyquote.com/topics/intelligence-quotes_3',
    'http://www.brainyquote.com/topics/alone-quotes_2',
    'http://www.brainyquote.com/topics/money-quotes_2',
    'http://www.brainyquote.com/topics/life-quotes_12',
    'http://www.brainyquote.com/topics/moving-on-quotes_7',
    'http://www.brainyquote.com/topics/intelligence-quotes_4',
    'http://www.brainyquote.com/topics/imagination-quotes_7',
    'http://www.brainyquote.com/topics/alone-quotes_3',
    'http://www.brainyquote.com/topics/life-quotes_13',
    'http://www.brainyquote.com/topics/money-quotes_3',
    'http://www.brainyquote.com/topics/intelligence-quotes_5',
    'http://www.brainyquote.com/topics/imagination-quotes_8',
    'http://www.brainyquote.com/topics/alone-quotes_4',
    'http://www.brainyquote.com/topics/life-quotes_14',
    'http://www.brainyquote.com/topics/moving-on-quotes_8',
    'http://www.brainyquote.com/topics/money-quotes_4',
    'http://www.brainyquote.com/topics/intelligence-quotes_6',
    'http://www.brainyquote.com/topics/imagination-quotes_9',
    'http://www.brainyquote.com/topics/alone-quotes_5',
    'http://www.brainyquote.com/topics/alone-quotes_7',
    'http://www.brainyquote.com/topics/money-quotes_5',
    'http://www.brainyquote.com/topics/imagination-quotes_10',
    'http://www.brainyquote.com/topics/imagination-quotes_0',
    'http://www.brainyquote.com/topics/alone-quotes_6',
    'http://www.brainyquote.com/topics/moving-on-quotes_9',
    'http://www.brainyquote.com/topics/alone-quotes_8',
    'http://www.brainyquote.com/topics/money-quotes_6',
    'http://www.brainyquote.com/topics/positive-quotes_0',
    'http://www.brainyquote.com/topics/imagination-quotes_11',
    'http://www.brainyquote.com/topics/alone-quotes_9',
    'http://www.brainyquote.com/topics/moving-on-quotes_0',
    'http://www.brainyquote.com/topics/imagination-quotes_12',
    'http://www.brainyquote.com/topics/imagination-quotes_1',
    'http://www.brainyquote.com/topics/moving-on-quotes_10',
    'http://www.brainyquote.com/topics/positive-quotes_1',
    'http://www.brainyquote.com/topics/alone-quotes_10',
    'http://www.brainyquote.com/topics/imagination-quotes_13',
    'http://www.brainyquote.com/topics/moving-on-quotes_1',
    'http://www.brainyquote.com/topics/imagination-quotes_2',
    'http://www.brainyquote.com/topics/moving-on-quotes_11',
    'http://www.brainyquote.com/topics/imagination-quotes_14',
    'http://www.brainyquote.com/topics/alone-quotes_11',
    'http://www.brainyquote.com/topics/imagination-quotes_3',
    'http://www.brainyquote.com/topics/humor-quotes_7',
    'http://www.brainyquote.com/topics/positive-quotes_2',
    'http://www.brainyquote.com/topics/alone-quotes_12',
    'http://www.brainyquote.com/topics/moving-on-quotes_2',
    'http://www.brainyquote.com/topics/moving-on-quotes_12',
    'http://www.brainyquote.com/topics/imagination-quotes_4',
    'http://www.brainyquote.com/topics/humor-quotes_8',
    'http://www.brainyquote.com/topics/positive-quotes_3',
    'http://www.brainyquote.com/topics/moving-on-quotes_3',
    'http://www.brainyquote.com/topics/alone-quotes_13',
    'http://www.brainyquote.com/topics/imagination-quotes_5',
    'http://www.brainyquote.com/topics/humor-quotes_9',
    'http://www.brainyquote.com/topics/positive-quotes_4',
    'http://www.brainyquote.com/topics/moving-on-quotes_4',
    'http://www.brainyquote.com/topics/moving-on-quotes_13',
    'http://www.brainyquote.com/topics/alone-quotes_14',
    'http://www.brainyquote.com/topics/imagination-quotes_6',
    'http://www.brainyquote.com/topics/humor-quotes_10',
    'http://www.brainyquote.com/topics/moving-on-quotes_5',
    'http://www.brainyquote.com/topics/positive-quotes_5',
    'http://www.brainyquote.com/topics/humor-quotes_0',
    'http://www.brainyquote.com/topics/moving-on-quotes_14',
    'http://www.brainyquote.com/topics/humor-quotes_11',
    'http://www.brainyquote.com/topics/positive-quotes_7',
    'http://www.brainyquote.com/topics/positive-quotes_6',
    'http://www.brainyquote.com/topics/humor-quotes_12',
    'http://www.brainyquote.com/topics/positive-quotes_8',
    'http://www.brainyquote.com/topics/moving-on-quotes_6',
    'http://www.brainyquote.com/topics/humor-quotes_1',
    'http://www.brainyquote.com/topics/positive-quotes_7',
    'http://www.brainyquote.com/topics/humor-quotes_13',
    'http://www.brainyquote.com/topics/positive-quotes_9',
    'http://www.brainyquote.com/topics/positive-quotes_8',
    'http://www.brainyquote.com/topics/dreams-quotes_0',
    'http://www.brainyquote.com/topics/positive-quotes_0',
    'http://www.brainyquote.com/topics/humor-quotes_2',
    'http://www.brainyquote.com/topics/humor-quotes_14',
    'http://www.brainyquote.com/topics/positive-quotes_9',
    'http://www.brainyquote.com/topics/positive-quotes_10',
    'http://www.brainyquote.com/topics/hope-quotes_7',
    'http://www.brainyquote.com/topics/humor-quotes_3',
    'http://www.brainyquote.com/topics/positive-quotes_10',
    'http://www.brainyquote.com/topics/positive-quotes_11',
    'http://www.brainyquote.com/topics/dreams-quotes_1',
    'http://www.brainyquote.com/topics/positive-quotes_1',
    'http://www.brainyquote.com/topics/hope-quotes_8',
    'http://www.brainyquote.com/topics/humor-quotes_4',
    'http://www.brainyquote.com/topics/positive-quotes_12',
    'http://www.brainyquote.com/topics/positive-quotes_11',
    'http://www.brainyquote.com/topics/hope-quotes_9',
    'http://www.brainyquote.com/topics/humor-quotes_5',
    'http://www.brainyquote.com/topics/dreams-quotes_2',
    'http://www.brainyquote.com/topics/positive-quotes_2',
    'http://www.brainyquote.com/topics/positive-quotes_13',
    'http://www.brainyquote.com/topics/hope-quotes_10',
    'http://www.brainyquote.com/topics/positive-quotes_12',
    'http://www.brainyquote.com/topics/humor-quotes_6',
    'http://www.brainyquote.com/topics/positive-quotes_3',
    'http://www.brainyquote.com/topics/dreams-quotes_3',
    'http://www.brainyquote.com/topics/hope-quotes_11',
    'http://www.brainyquote.com/topics/hope-quotes_0',
    'http://www.brainyquote.com/topics/positive-quotes_13',
    'http://www.brainyquote.com/topics/positive-quotes_14',
    'http://www.brainyquote.com/topics/positive-quotes_4',
    'http://www.brainyquote.com/topics/hope-quotes_12',
    'http://www.brainyquote.com/topics/positive-quotes_14',
    'http://www.brainyquote.com/topics/dreams-quotes_7',
    'http://www.brainyquote.com/topics/dreams-quotes_4',
    'http://www.brainyquote.com/topics/hope-quotes_1',
    'http://www.brainyquote.com/topics/hope-quotes_13',
    'http://www.brainyquote.com/topics/work-quotes_7',
    'http://www.brainyquote.com/topics/dreams-quotes_8',
    'http://www.brainyquote.com/topics/dreams-quotes_5',
    'http://www.brainyquote.com/topics/positive-quotes_5',
    'http://www.brainyquote.com/topics/hope-quotes_14',
    'http://www.brainyquote.com/topics/dreams-quotes_6',
    'http://www.brainyquote.com/topics/work-quotes_8',
    'http://www.brainyquote.com/topics/dreams-quotes_9',
    'http://www.brainyquote.com/topics/positive-quotes_6',
    'http://www.brainyquote.com/topics/hope-quotes_2',
    'http://www.brainyquote.com/topics/smile-quotes_0',
    'http://www.brainyquote.com/topics/god-quotes_7',
    'http://www.brainyquote.com/topics/work-quotes_9',
    'http://www.brainyquote.com/topics/work-quotes_0',
    'http://www.brainyquote.com/topics/dreams-quotes_10',
    'http://www.brainyquote.com/topics/hope-quotes_3',
    'http://www.brainyquote.com/topics/god-quotes_8',
    'http://www.brainyquote.com/topics/work-quotes_10',
    'http://www.brainyquote.com/topics/smile-quotes_1',
    'http://www.brainyquote.com/topics/dreams-quotes_11',
    'http://www.brainyquote.com/topics/hope-quotes_4',
    'http://www.brainyquote.com/topics/god-quotes_9',
    'http://www.brainyquote.com/topics/work-quotes_1',
    'http://www.brainyquote.com/topics/work-quotes_11',
    'http://www.brainyquote.com/topics/hope-quotes_5',
    'http://www.brainyquote.com/topics/god-quotes_10',
    'http://www.brainyquote.com/topics/dreams-quotes_12',
    'http://www.brainyquote.com/topics/smile-quotes_2',
    'http://www.brainyquote.com/topics/work-quotes_12',
    'http://www.brainyquote.com/topics/god-quotes_11',
    'http://www.brainyquote.com/topics/hope-quotes_6',
    'http://www.brainyquote.com/topics/dreams-quotes_13',
    'http://www.brainyquote.com/topics/work-quotes_2',
    'http://www.brainyquote.com/topics/work-quotes_13',
    'http://www.brainyquote.com/topics/smile-quotes_3',
    'http://www.brainyquote.com/topics/god-quotes_12',
    'http://www.brainyquote.com/topics/god-quotes_0',
    'http://www.brainyquote.com/topics/dreams-quotes_14',
    'http://www.brainyquote.com/topics/work-quotes_3',
    'http://www.brainyquote.com/topics/work-quotes_14',
    'http://www.brainyquote.com/topics/smile-quotes_4',
    'http://www.brainyquote.com/topics/god-quotes_13',
    'http://www.brainyquote.com/topics/smile-quotes_7',
    'http://www.brainyquote.com/topics/work-quotes_4',
    'http://www.brainyquote.com/topics/truth-quotes_7',
    'http://www.brainyquote.com/topics/god-quotes_1',
    'http://www.brainyquote.com/topics/smile-quotes_5',
    'http://www.brainyquote.com/topics/god-quotes_14',
    'http://www.brainyquote.com/topics/work-quotes_5',
    'http://www.brainyquote.com/topics/smile-quotes_8',
    'http://www.brainyquote.com/topics/truth-quotes_8',
    'http://www.brainyquote.com/topics/smile-quotes_6',
    'http://www.brainyquote.com/topics/work-quotes_6',
    'http://www.brainyquote.com/topics/god-quotes_2',
    'http://www.brainyquote.com/topics/truth-quotes_9',
    'http://www.brainyquote.com/topics/smile-quotes_9',
    'http://www.brainyquote.com/topics/future-quotes_7',
    'http://www.brainyquote.com/topics/experience-quotes_0',
    'http://www.brainyquote.com/topics/god-quotes_3',
    'http://www.brainyquote.com/topics/truth-quotes_0',
    'http://www.brainyquote.com/topics/smile-quotes_10',
    'http://www.brainyquote.com/topics/future-quotes_8',
    'http://www.brainyquote.com/topics/truth-quotes_10',
    'http://www.brainyquote.com/topics/god-quotes_4',
    'http://www.brainyquote.com/topics/smile-quotes_11',
    'http://www.brainyquote.com/topics/future-quotes_9',
    'http://www.brainyquote.com/topics/experience-quotes_1',
    'http://www.brainyquote.com/topics/truth-quotes_1',
    'http://www.brainyquote.com/topics/truth-quotes_11',
    'http://www.brainyquote.com/topics/god-quotes_5',
    'http://www.brainyquote.com/topics/smile-quotes_12',
    'http://www.brainyquote.com/topics/future-quotes_10',
    'http://www.brainyquote.com/topics/truth-quotes_12',
    'http://www.brainyquote.com/topics/smile-quotes_13',
    'http://www.brainyquote.com/topics/god-quotes_6',
    'http://www.brainyquote.com/topics/future-quotes_11',
    'http://www.brainyquote.com/topics/experience-quotes_2',
    'http://www.brainyquote.com/topics/truth-quotes_2',
    'http://www.brainyquote.com/topics/truth-quotes_13',
    'http://www.brainyquote.com/topics/smile-quotes_14',
    'http://www.brainyquote.com/topics/future-quotes_0',
    'http://www.brainyquote.com/topics/future-quotes_12',
    'http://www.brainyquote.com/topics/experience-quotes_3',
    'http://www.brainyquote.com/topics/truth-quotes_3',
    'http://www.brainyquote.com/topics/experience-quotes_7',
    'http://www.brainyquote.com/topics/truth-quotes_14',
    'http://www.brainyquote.com/topics/future-quotes_1',
    'http://www.brainyquote.com/topics/truth-quotes_4',
    'http://www.brainyquote.com/topics/future-quotes_13',
    'http://www.brainyquote.com/topics/experience-quotes_8',
    'http://www.brainyquote.com/topics/experience-quotes_4',
    'http://www.brainyquote.com/topics/travel-quotes_7',
    'http://www.brainyquote.com/topics/truth-quotes_5',
    'http://www.brainyquote.com/topics/future-quotes_14',
    'http://www.brainyquote.com/topics/experience-quotes_9',
    'http://www.brainyquote.com/topics/future-quotes_2',
    'http://www.brainyquote.com/topics/experience-quotes_5',
    'http://www.brainyquote.com/topics/travel-quotes_8',
    'http://www.brainyquote.com/topics/truth-quotes_6',
    'http://www.brainyquote.com/topics/love-quotes_7',
    'http://www.brainyquote.com/topics/experience-quotes_10',
    'http://www.brainyquote.com/topics/future-quotes_3',
    'http://www.brainyquote.com/topics/experience-quotes_6',
    'http://www.brainyquote.com/topics/travel-quotes_9',
    'http://www.brainyquote.com/topics/love-quotes_8',
    'http://www.brainyquote.com/topics/experience-quotes_11',
    'http://www.brainyquote.com/topics/future-quotes_4',
    'http://www.brainyquote.com/topics/travel-quotes_10',
    'http://www.brainyquote.com/topics/failure-quotes_0',
    'http://www.brainyquote.com/topics/future-quotes_5',
    'http://www.brainyquote.com/topics/experience-quotes_12',
    'http://www.brainyquote.com/topics/travel-quotes_11',
    'http://www.brainyquote.com/topics/love-quotes_9',
    'http://www.brainyquote.com/topics/travel-quotes_0',
    'http://www.brainyquote.com/topics/future-quotes_6',
    'http://www.brainyquote.com/topics/experience-quotes_13',
    'http://www.brainyquote.com/topics/travel-quotes_12',
    'http://www.brainyquote.com/topics/love-quotes_10',
    'http://www.brainyquote.com/topics/failure-quotes_1',
    'http://www.brainyquote.com/topics/experience-quotes_14',
    'http://www.brainyquote.com/topics/love-quotes_0',
    'http://www.brainyquote.com/topics/travel-quotes_13',
    'http://www.brainyquote.com/topics/love-quotes_11',
    'http://www.brainyquote.com/topics/travel-quotes_1',
    'http://www.brainyquote.com/topics/failure-quotes_7',
    'http://www.brainyquote.com/topics/travel-quotes_14',
    'http://www.brainyquote.com/topics/love-quotes_12',
    'http://www.brainyquote.com/topics/failure-quotes_2',
    'http://www.brainyquote.com/topics/failure-quotes_8',
    'http://www.brainyquote.com/topics/time-quotes_7',
    'http://www.brainyquote.com/topics/love-quotes_13',
    'http://www.brainyquote.com/topics/love-quotes_1',
    'http://www.brainyquote.com/topics/failure-quotes_3',
    'http://www.brainyquote.com/topics/travel-quotes_2',
    'http://www.brainyquote.com/topics/failure-quotes_9',
    'http://www.brainyquote.com/topics/time-quotes_8',
    'http://www.brainyquote.com/topics/love-quotes_14',
    'http://www.brainyquote.com/topics/failure-quotes_4',
    'http://www.brainyquote.com/topics/travel-quotes_3',
    'http://www.brainyquote.com/topics/love-quotes_2',
    'http://www.brainyquote.com/topics/failure-quotes_10',
    'http://www.brainyquote.com/topics/failure-quotes_5',
    'http://www.brainyquote.com/topics/time-quotes_9',
    'http://www.brainyquote.com/topics/travel-quotes_4',
    'http://www.brainyquote.com/topics/love-quotes_3',
    'http://www.brainyquote.com/topics/failure-quotes_11',
    'http://www.brainyquote.com/topics/failure-quotes_6',
    'http://www.brainyquote.com/topics/time-quotes_10',
    'http://www.brainyquote.com/topics/travel-quotes_5',
    'http://www.brainyquote.com/topics/love-quotes_4',
    'http://www.brainyquote.com/topics/failure-quotes_12',
    'http://www.brainyquote.com/topics/faith-quotes_0',
    'http://www.brainyquote.com/topics/time-quotes_11',
    'http://www.brainyquote.com/topics/travel-quotes_6',
    'http://www.brainyquote.com/topics/love-quotes_5',
    'http://www.brainyquote.com/topics/failure-quotes_13',
    'http://www.brainyquote.com/topics/time-quotes_0',
    'http://www.brainyquote.com/topics/time-quotes_12',
    'http://www.brainyquote.com/topics/love-quotes_6',
    'http://www.brainyquote.com/topics/failure-quotes_14',
    'http://www.brainyquote.com/topics/faith-quotes_1',
    'http://www.brainyquote.com/topics/time-quotes_13',
    'http://www.brainyquote.com/topics/faith-quotes_7',
    'http://www.brainyquote.com/topics/time-quotes_1',
    'http://www.brainyquote.com/topics/time-quotes_14',
    'http://www.brainyquote.com/topics/faith-quotes_8',
    'http://www.brainyquote.com/topics/faith-quotes_2',
    'http://www.brainyquote.com/topics/faith-quotes_9',
    'http://www.brainyquote.com/topics/faith-quotes_3',
    'http://www.brainyquote.com/topics/time-quotes_2',
    'http://www.brainyquote.com/topics/faith-quotes_10',
    'http://www.brainyquote.com/topics/faith-quotes_4',
    'http://www.brainyquote.com/topics/time-quotes_3',
    'http://www.brainyquote.com/topics/faith-quotes_11',
    'http://www.brainyquote.com/topics/faith-quotes_5',
    'http://www.brainyquote.com/topics/time-quotes_4',
    'http://www.brainyquote.com/topics/faith-quotes_12',
    'http://www.brainyquote.com/topics/faith-quotes_6',
    'http://www.brainyquote.com/topics/time-quotes_5',
    'http://www.brainyquote.com/topics/faith-quotes_13',
    'http://www.brainyquote.com/topics/time-quotes_6',
    'http://www.brainyquote.com/topics/faith-quotes_14',
    'http://www.brainyquote.com/topics/motivational-quotes',
    'http://www.brainyquote.com/topics/famous-quotes',
    'http://www.brainyquote.com/topics/marriage-quotes',
    'http://www.brainyquote.com/topics/technology-quotes',
    'http://www.brainyquote.com/topics/motivational-quotes_0',
    'http://www.brainyquote.com/topics/motivational-quotes_7',
    'http://www.brainyquote.com/topics/famous-quotes_0',
    'http://www.brainyquote.com/topics/famous-quotes_7',
    'http://www.brainyquote.com/topics/marriage-quotes_0',
    'http://www.brainyquote.com/topics/technology-quotes_0',
]
quotes_list = []


def get_authors():
    global urlsList
    base_url = 'http://www.brainyquote.com'
    url_string = 'http://www.brainyquote.com/topics/'
    topics = [
        'motivational-quotes',
        'inspirational-quotes',
        'life-quotes',
        'alone-quotes',
        'positive-quotes',
        'dreams-quotes',
        'smile-quotes',
        'experience-quotes',
        'failure-quotes',
        'faith-quotes',
        'famous-quotes',
        'change-quotes',
        'chance-quotes',
        'intelligence-quotes',
        'imagination-quotes',
        'humor-quotes',
        'hope-quotes',
        'god-quotes',
        'future-quotes',
        'love-quotes',
        'marriage-quotes',
        'knowledge-quotes',
        'leadership-quotes',
        'money-quotes',
        'moving-on-quotes',
        'positive-quotes',
        'work-quotes',
        'truth-quotes',
        'travel-quotes',
        'time-quotes',
        'technology-quotes',
        'success-quotes',
        'teacher-quotes',
    ]
    topics_url = [url_string + x for x in topics]
    print("")
    print("Scanning Started for page links")
    print("")

    def th1():
        for url in topics_url[:10]:
            print("Scanning URL: %s" % url)
            urlsList.append(url)
            urlsList.extend(pagination(url, False))

    def th2():
        for url in topics_url[10:20]:
            print("Scanning URL: %s" % url)
            urlsList.append(url)
            urlsList.extend(pagination(url, False))

    def th3():
        for url in topics_url[20:30]:
            print("Scanning URL: %s" % url)
            urlsList.append(url)
            urlsList.extend(pagination(url, False))

    def th4():
        for url in topics_url[30:34]:
            print("Scanning URL: %s" % url)
            urlsList.append(url)
            urlsList.extend(pagination(url, False))

    th1 = threading.Thread(target=th1)
    th2 = threading.Thread(target=th2)
    th3 = threading.Thread(target=th3)
    th4 = threading.Thread(target=th4)
    th1.start()
    th2.start()
    th3.start()
    th4.start()

    def tu1():
        def c1():
            for url in topics_url[:10]:
                for count in range(7):
                    # try:
                    url_pages = f'{url}_{count}'
                    print(f"Scanning URL: {url}_{count}")
                    urlsList.append(url_pages)
                    urlsList.extend(pagination(url_pages, False))

        def c2():
            for url in topics_url[:10]:
                for count in range(7, 15):
                    # try:
                    url_pages = f'{url}_{count}'
                    print(f"Scanning URL: {url}_{count}")
                    urlsList.append(url_pages)
                    urlsList.extend(pagination(url_pages, False))

        ct1 = threading.Thread(target=c1)
        ct2 = threading.Thread(target=c2)
        ct1.start()
        ct2.start()

    def tu2():
        def c1():
            for url in topics_url[10:20]:
                for count in range(7):
                    # try:
                    url_pages = f'{url}_{count}'
                    print(f"Scanning URL: {url}_{count}")
                    urlsList.append(url_pages)
                    urlsList.extend(pagination(url_pages, False))

        def c2():
            for url in topics_url[10:20]:
                for count in range(7, 15):
                    # try:
                    url_pages = f'{url}_{count}'
                    print(f"Scanning URL: {url}_{count}")
                    urlsList.append(url_pages)
                    urlsList.extend(pagination(url_pages, False))

        ct1 = threading.Thread(target=c1)
        ct2 = threading.Thread(target=c2)
        ct1.start()
        ct2.start()

    def tu3():
        def c1():
            for url in topics_url[20:30]:
                for count in range(7):
                    # try:
                    url_pages = f'{url}_{count}'
                    print(f"Scanning URL: {url}_{count}")
                    urlsList.append(url_pages)
                    urlsList.extend(pagination(url_pages, False))

        def c2():
            for url in topics_url[20:30]:
                for count in range(7, 15):
                    # try:
                    url_pages = f'{url}_{count}'
                    print(f"Scanning URL: {url}_{count}")
                    urlsList.append(url_pages)
                    urlsList.extend(pagination(url_pages, False))

        ct1 = threading.Thread(target=c1)
        ct2 = threading.Thread(target=c2)
        ct1.start()
        ct2.start()

    def tu4():
        def c1():
            for url in topics_url[30:34]:
                for count in range(7):
                    # try:
                    url_pages = f'{url}_{count}'
                    print(f"Scanning URL: {url}_{count}")
                    urlsList.append(url_pages)
                    urlsList.extend(pagination(url_pages, False))

        def c2():
            for url in topics_url[30:34]:
                for count in range(7, 15):
                    # try:
                    url_pages = f'{url}_{count}'
                    print(f"Scanning URL: {url}_{count}")
                    urlsList.append(url_pages)
                    urlsList.extend(pagination(url_pages, False))

        ct1 = threading.Thread(target=c1)
        ct2 = threading.Thread(target=c2)
        ct1.start()
        ct2.start()

    t1 = threading.Thread(target=tu1)
    t2 = threading.Thread(target=tu2)
    t3 = threading.Thread(target=tu3)
    t4 = threading.Thread(target=tu4)
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    print("")
    print("All Done \nThanks for using it...!!!")
    print("")

    print('I am printing in the back')
    with open('quotes_urls.txt', 'w') as qua:
        for url in urlsList:
            qua.write(f"{url.encode('utf-8')} \n")
        qua.close()
    print("")
    print("Scanning Started for fetching quotes")
    print("")


def get_authors_links(url):
    page = requests.get(url)
    tree = html.fromstring(page.text)
    arr = tree.xpath('//table[@class="table table-hover table-bordered"]//td/a/@href')
    return arr


def fetch_quote(url, num):
    try:
        page = requests.get(url)
        tree = html.fromstring(page.text)
        quotes = tree.find_class('bqQt')
        quotes_file = f'quotes_{num}.txt'
        with open(quotes_file, 'a') as qw:
            for q in quotes:
                quote = next(q.find_class('b-qt')[0].iter('a')).text
                author = next(q.find_class('bq-aut')[0].iter('a')).text
                qw.write(f'"{quote}" : "{author}",\n')
            print('Some Scraping Completed')
    except OSError:
        pass


def pagination(url, htmlPage):  # .html or not - htmlPage True or False
    arr = []
    page = requests.get(url)
    tree = html.fromstring(page.text)
    end = tree.xpath('//div[@class="row paginationContainer"]//nav//ul/li[last()-1]/a/text()')
    if len(end):
        if htmlPage:
            url = url.split('.html')[0]
            for count in range(2, int(end[0]) + 1):
                arr.append(url + "%s.html" % (count))
        else:
            for count in range(2, int(end[0]) + 1):
                arr.append(url + "%s" % (count))
    return arr


if __name__ == '__main__':
    # get_authors()
    try:
        def url_thread1():
            for url in urlsList[:50]:
                fetch_quote(url, 1)
            print('Diabolical')


        def url_thread2():
            for url in urlsList[50:100]:
                fetch_quote(url, 2)
            print('Diabolical')


        def url_thread3():
            for url in urlsList[150:200]:
                fetch_quote(url, 3)
            print('Diabolical')


        def url_thread4():
            for url in urlsList[200:250]:
                fetch_quote(url, 4)
            print('Diabolical')


        def url_thread5():
            for url in urlsList[250:300]:
                fetch_quote(url, 5)
            print('Diabolical')


        def url_thread6():
            for url in urlsList[300:350]:
                fetch_quote(url, 6)
            print('Diabolical')


        def url_thread7():
            for url in urlsList[350:400]:
                fetch_quote(url, 7)
            print('Diabolical')


        def url_thread8():
            for url in urlsList[400:450]:
                fetch_quote(url, 8)
            print('Diabolical')


        def url_thread9():
            for url in urlsList[450:500]:
                fetch_quote(url, 9)
            print('Diabolical')


        def url_thread10():
            for url in urlsList[500:526]:
                fetch_quote(url, 10)
            print('Diabolical')


        ur1 = threading.Thread(target=url_thread1)
        ur2 = threading.Thread(target=url_thread2)
        ur3 = threading.Thread(target=url_thread3)
        ur4 = threading.Thread(target=url_thread4)
        ur5 = threading.Thread(target=url_thread5)
        ur6 = threading.Thread(target=url_thread6)
        ur7 = threading.Thread(target=url_thread7)
        ur8 = threading.Thread(target=url_thread8)
        ur9 = threading.Thread(target=url_thread9)
        ur10 = threading.Thread(target=url_thread10)

        ur1.start()
        ur2.start()
        ur3.start()
        ur4.start()
        ur5.start()
        ur6.start()
        ur7.start()
        ur8.start()
        ur9.start()
        ur10.start()

    except IndexError:
        pass
