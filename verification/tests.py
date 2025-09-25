"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": ["Succulent", 11, True],
            "answer": "Do not water",
        },
        {
            "input": ["Tropical", 3, False],
            "answer": "Check the soil again tomorrow",
        },
        {
            "input": ["Default", 8, False],
            "answer": "Water the plant",
        },
        {
            "input": ["Plant", 8, False],
            "answer": "Unknown plant type",
        },
    ],
    "Extra": [
        {
            "input": ["Succulent", 11, False],
            "answer": "Do not water",
        },
        {
            "input": ["Succulent", 12, True],
            "answer": "Do not water",
        },
        {
            "input": ["Succulent", 12, False],
            "answer": "Check the soil again tomorrow",
        },
        {
            "input": ["Succulent", 13, True],
            "answer": "Do not water",
        },
        {
            "input": ["Succulent", 13, False],
            "answer": "Water the plant",
        },
        {
            "input": ["Tropical", 2, True],
            "answer": "Do not water",
        },
        {
            "input": ["Tropical", 2, False],
            "answer": "Do not water",
        },
        {
            "input": ["Tropical", 3, True],
            "answer": "Do not water",
        },
        {
            "input": ["Tropical", 4, True],
            "answer": "Do not water",
        },
        {
            "input": ["Tropical", 4, False],
            "answer": "Water the plant",
        },
        {
            "input": ["Default", 6, True],
            "answer": "Do not water",
        },
        {
            "input": ["Default", 6, False],
            "answer": "Do not water",
        },
        {
            "input": ["Default", 7, True],
            "answer": "Do not water",
        },
        {
            "input": ["Default", 7, False],
            "answer": "Check the soil again tomorrow",
        },
        {
            "input": ["Default", 8, True],
            "answer": "Do not water",
        },
    ]
}
