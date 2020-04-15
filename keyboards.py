import json

# KEYBOARD_1 = {
#     "one_time": False,
#     "buttons": [
#         [{
#             "action": {
#                 "type": "text",
#                 "payload": json.dumps(''),
#                 "label": "Правила"
#             },
#             "color": "primary"
#         }],
#         [{
#             "action": {
#                 "type": "text",
#                 "payload": json.dumps(''),
#                 "label": "Узнать дату и время"
#             },
#             "color": "positive"
#         }]
#         ]
#     }

KEYBOARD = {
    "one_time": False,
    "buttons": [
        [{
            "action": {
                "type": "text",
                "payload": json.dumps(''),
                "label": "Курсы валют"
            },
            "color": "primary"
        }],
        [{
            "action": {
                "type": "text",
                "payload": json.dumps(''),
                "label": "Узнать дату и время"
            },
            "color": "primary"
        }],
        [{
            "action": {
                "type": "text",
                "payload": json.dumps(''),
                "label": "Правила"
            },
            "color": "secondary"
        }]
    ]
    }

KEYBOARD_2 = {
    "one_time": False,
    "buttons": [
        [{
            "action": {
                "type": "text",
                "payload": json.dumps(''),
                "label": "Доллар"
            },
            "color": "positive"
        }],
        [{
            "action": {
                "type": "text",
                "payload": json.dumps(''),
                "label": "Евро"
            },
            "color": "positive"
        }],
        [{
            "action": {
                "type": "text",
                "payload": json.dumps(''),
                "label": "Гривна"
            },
            "color": "positive"
        }],
        [{
            "action": {
                "type": "text",
                "payload": json.dumps(''),
                "label": "Назад"
            },
            "color": "negative"
        }]
    ]
    }