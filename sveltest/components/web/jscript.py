


class JSElement(object):
    def __init__(self,driver):
        self.driver = driver

    def click(self,class_name=None,id=None,name=None,
                     index=None,describe=None):
        describe = describe
        if class_name:
            class_name = """document.getElementsByClassName("{classname}")
            [{index}].click(); 
            """.format(classname=class_name,index=index)
            d = self.driver.execute_script(class_name)

            return class_name

        if id:

           id =  f"""document.getElementById("{id}").click();"""
           f = self.driver.execute_script(id)
           return name


        if name:
           name =  """document.getElementsByName("{name}")
           [{index}].click();""".format(name=name,index=index)
           return name



    def input(self, id=None,name=None,classname=None, index=None,value=None,describe=None):
        if id:
            id = f"""document.getElementById("{id}").value = "{value}";"""
            self.driver.execute_script(id)
            return id

        describe = describe
        class_name = """document.getElementsByClassName("{classname}")
        ["{index}"].value="{value}"; 
        """.format(classname=classname, index=index,value=value)
        self.driver.execute_script(class_name)

        return class_name

class BrowserObject(object):
    """
    该模类是对javascript 的BOM模型进行封装也就是我们还不能制作一些我们经常看
    到的网页的一些交互，我们需要继续学习BOM和DOM相关知识。
    JavaScript分为 ECMAScript，DOM，BOM。
    BOM（Browser Object Model）是指浏览器对象模型，它使 JavaScript 有能力与
    浏览器进行“对话”。
    """
    #This module class encapsulates the bom model of javascript, that is, we
    # can not make some interactions of the web pages we often see, and we
    # need to continue to learn bom and dom related knowledge. Javascript is
    # divided into ecmascript,dom,bom. Bom (browser object model) refers to
    # the browser object model, which enables javascript to have a "dialogue"
    # with the browser

    def __init__(self,driver):
        self.driver = driver


    def window_height(self,describe=None):
        describe = describe
        win = """var name = window.innerHeight;
                    console.log(name)"""
        win_height = self.driver.execute_script(win)
        return win_height

    def window_open(self,describe=None):
        describe = describe
        win = "window.open();"
        win_Open = self.driver.execute_script(win)
        return win_Open

    def window_close(self,describe=None):
        describe = describe
        win = "window.close();"
        win_close= self.driver.execute_script(win)
        return win_close

    def add_element(self,type=None,tag_name=None,index=None,types=None,
                    values=None,describe=None):
        if tag_name:
            describe = describe
            win = """document.getElementsByTagName
            ("{tagname}")[{indexs}].setAttribute("{types}","{value}");
            """.format(tagname=tag_name,indexs=index,types=types,value=values)
            win_close= self.driver.execute_script(win)

            return win_close

