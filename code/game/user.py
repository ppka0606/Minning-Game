import json

class User():
    """
    用来管理用户的信息(用户名,每种角色的最高分等)
    与Maze一样,只提供接口,不直接负责呈现在界面上
    """
    @staticmethod
    def get_user_list():
        """
        读取玩家列表,作为静态方法
        """
        user_dict = {}
        try:
            with open(r"resource/mingingGame/User/MiningGame_user_list.json","r") as user_list_json:
                user_dict = json.load(user_list_json)
                user_list_json.close()
        except FileNotFoundError:
        # 注意:如果文件不存在必须在创建的文件中写入{},因为json.load可以解析空对象而不能解析空文档
            with open(r"resource/mingingGame/User/MiningGame_user_list.json", "w") as user_list_json:
                user_list_json.write(json.dumps(user_dict))
                user_list_json.close()
        except json.JSONDecodeError:
            # 同样,如果出现json文件格式损坏,同上操作
            # 清空json文件并重新写入一个空对象
            # 另外,由于这种错误对象是在json包里面的,所以必须有前缀
            with open(r"resource/mingingGame/User/MiningGame_user_list.json", "w") as user_list_json:
                user_list_json.write(json.dumps(user_dict))
                user_list_json.close()

    def __init__(self, name):
        pass

            