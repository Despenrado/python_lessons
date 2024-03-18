import functools

def project():
    tasks = {}
    deps = {}
    
    def register(func=None, *,depends_on = []):
        if func is None:
            return lambda f: register(f, depends_on=depends_on)
        
        def exec_deps(func_name):
            for dep_name in deps.get(func_name):
                task = tasks.get(dep_name)
                if task:
                    task()
        
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            exec_deps(func.__name__)
            return func(*args, **kwargs)
        
        tasks[func.__name__] = func
        deps[func.__name__] = depends_on
        
        wrapper.get_dependencies = lambda: deps.get(func.__name__)
        
        return wrapper
    
    register.get_all = lambda: list(tasks)

    return register


register = project()

@register
def do_smth():
    print("do_smth")


@register(depends_on=["do_smth"])
def do_smth_v2():
    print("do_smth_v2")


print(register.get_all())
do_smth()
do_smth_v2()

print(do_smth.get_dependencies())
print(do_smth_v2.get_dependencies())
