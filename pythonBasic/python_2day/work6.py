"""
字典操作方法：
1.get
2.keys
"""
f = {
    "名字": "sqh",
    "年龄": 18,
    "技能": {
        "技能1": "python",
        "技能2": "C++"
    }
}
print(f.keys()) # dict_keys(['名字', '年龄'])
print(f.get("技能").keys()) # dict_keys(['技能1', '技能2'])