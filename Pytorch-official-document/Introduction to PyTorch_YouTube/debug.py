# __all__ = ['create_param_saver', 'ParamSaver']

import copy
def create_param_saver(target_step):
    """
    工厂函数：创建一个带有内部计数器的参数保存器
    """
    counter = 0  # 内部维护的计数器
    
    def copy_params(*args):
        nonlocal counter  # 声明使用外部闭包变量
        counter += 1      # 每次调用自动 +1
        print(counter, target_step)
        
        # 达到目标次数时，执行深拷贝并返回
        if counter == target_step:
            return tuple(copy.deepcopy(arg) for arg in args)
        return None  # 未达到目标次数，返回 None
        
    return copy_params


class ParamSaver:
    def __init__(self, target_step):
        self.target_step = target_step
        self.counter = 0
        self.saved_params = []  # 内部自动收集结果

    def step(self, *args):
        """每次迭代时调用"""
        self.counter += 1
        if self.counter == self.target_step:
            snapshot = tuple(copy.deepcopy(arg) for arg in args)
            self.saved_params.append(snapshot)
            self.counter = 0  # 自动重置，支持多次保存

    def get_params(self):
        """获取保存的参数"""
        return self.saved_params
    
