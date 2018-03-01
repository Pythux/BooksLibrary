{
    "yo": "value",
    "li": [1, 2, 3],
    "obj": {
        "txt": "Text",
        "nb": 42
    },
    "li_obj": [
        { "id": 1, "txt": "one" },
        { "id": 2, "txt": "two" }
    ],
    "li_all": [
        4,
        "yo",
        { "obj": true, "data": "long text\nvery very\nlong" }
    ]
}

# in YAML:

yo: value
li:
    - 1
    - 2
    - 3
li: [1, 2, 3]
obj:
    txt: Text
    nb: 42
li_obj:
    - id: 1
      txt: one

    - id: 2
      txt: two
li_all:
    - 4
    - yo
    - obj: true
      data: |
        long text
        very very
        long

or:

li_all:
    - 4
    - yo
    - obj: true
      data: >
        long
        text\nvery
        very\nlong
