'''我的首页'''
import streamlit as st
from PIL import Image

page = st.sidebar.radio('我的首页', ['我的兴趣推荐', '我的图片处理工具', '我的智慧词典', '我的留言区'])

def page_1():
    '''我的推荐'''
    with open('霞光.mp3','rb')as f:
        mymp3=f.read()
    st.audio(mymp3,format='audio/mp3',start_time=0)
    st.image('slogan.png')
    st.write('我的电影推荐')
    st.write('-----------------------------')
    st.write('我的游戏推荐')
    st.write('-----------------------------')
    st.write('我的书籍推荐')
    st.write('-----------------------------')
    st.write('我的习题集推荐')
    st.write('-----------------------------')
    st.write('图片.jpg')
    #st.write("<span style='font-size:20px'>这是设置为20px字体大小的文本</span>", unsafe_allow_html=True)
    def pape_2():
        '''我的图片处理工具'''
        st.write(':sunglasses:图片换色小程序:sunglasses:')
        uploaded_file=st.file=st.file_uploader('上传图片',type=['png','jpeg','jpg'])
        if uploaded_file:
            #获取图片文件的名称,类型和大小。
            file_name=uploaded_file.name
            file_type=uploaded_file.type
            file_size=uploaded_file.size
            img=Image.open(uploaded_file)
            st.image(img)

def page_2():
    '''我的图片处理工具'''
    st.write(":sunglasses:图片换色小程序:sunglasses:")
    uploaded_file = st.file_uploader("上传图片", type=['png', 'jpeg', 'jpg'])
    if uploaded_file:
        # 获取图片文件的名称、类型和大小
        file_name = uploaded_file.name
        file_type = uploaded_file.type
        file_size = uploaded_file.size
        img = Image.open(uploaded_file)
        st.image(img)
        st.image(img_change(img, 0, 2, 1))

def page_3():
    '''我的智慧词典'''
    st.write('智慧词典')
    # 从本地文件中将词典信息读取出来，并存储在列表中
    with open('words_space.txt', 'r', encoding='utf-8') as f:
        words_list = f.read().split('\n')
    # 将列表中的每一项内容再进行分割，分为“编号、单词、解释”
    for i in range(len(words_list)):
        words_list[i] = words_list[i].split('#')
    # 将列表中的内容导入字典，方便查询，格式为“单词：编号、解释”
    words_dict = {}
    for i in words_list:
        words_dict[i[1]] = [int(i[0]), i[2]]
    # 从本地文件中将单词的查询次数读取出来，并存储在列表中
    with open('check_out_times.txt', 'r', encoding='utf-8') as f:
        times_list = f.read().split('\n')
    # 将列表转为字典
    for i in range(len(times_list)):
        times_list[i] = times_list[i].split('#')
    times_dict = {}
    for i in times_list:
        times_dict[int(i[0])] = int(i[1])
    # 创建输入框
    word = st.text_input('请输入要查询的单词')
    # 显示查询内容
    if word in words_dict:
        st.write(words_dict[word])
        n = words_dict[word][0]
        if n in times_dict:
            times_dict[n] += 1
        else:
            times_dict[n] = 1
        with open('check_out_times.txt', 'w', encoding='utf-8') as f:
            message = ''
            for k, v in times_dict.items():
                message += str(k) + '#' + str(v) + '\n'
            message = message[:-1]
            f.write(message)
        st.write('查询次数：', times_dict[n])
        if word == 'python':
            st.code('''
                    # 恭喜你触发彩蛋，这是一行python代码
                    print('hello world')''')
    # 滑动条st.slider()
    cb = st.checkbox('勾选选项')
    if cb:
        st.write('选项被勾选', cb)
    # 如何创建勾选框？
    # 勾选框更适合单选还是多选？
    # 勾选框的返回值是选框中的字符串吗？不是的话，返回值是什么？
    
    # 应用：宣传_互联网知识
    st.write('----')
    st.write('你知道吗：为什么要设置公网和私网？为什么不让每一个设备都直接连接到公网上？')
    cb1 = st.checkbox('易于管理')
    cb2 = st.checkbox('效率高')
    cb3 = st.checkbox('网速快')
    cb4 = st.checkbox('安全性好')
    l = [cb1, cb2, cb3, cb4]
    if st.button('确认答案'):
        if True in l:
            st.write('其实都不对，答案是“历史问题，不得已而为之”')
        else:
            st.write('好厉害！确实都不对，真实答案是“历史问题，不得已而为之”，下面就让我来讲讲吧：早期网络规模有限：在网络发展的早期，可用的 IP 地址资源相对充足，随着网络设备和用户数量的急剧增加，IP 地址变得稀缺。私网的出现可以在一定程度上缓解 IP 地址不足的问题，通过在私网内重复使用特定的私有 IP 地址段，提高了地址的利用率。
                    安全意识的逐渐形成：随着网络应用的普及，人们对网络安全的认识不断提高。在过去，网络攻击和信息泄露事件相对较少，但随着技术的发展，安全威胁日益严重。私网的设置为内部网络提供了一道屏障，降低了外部攻击的风险。例如，早期的企业网络可能没有明确的公网和私网划分，导致数据容易被窃取，后来逐渐形成了私网来保护重要信息。
                    成本和技术限制：在过去，网络建设和维护的成本较高，技术也相对不成熟。设置私网可以降低对公网资源的依赖，减少网络运营成本。同时，早期的网络技术在处理大规模网络流量和复杂的访问控制方面存在一定的局限性，私网的划分有助于简化网络管理和提高效率。行业和组织的特定需求：不同的行业和组织在发展过程中产生了各自独特的网络需求。例如，军事机构、政府部门等对信息安全要求极高，很早就开始采用私网来保护机密信息。而一些大型企业为了实现内部的高效协同和资源共享，也逐渐构建了私网环境。
                    这些历史原因促使了公网和私网的设置逐渐成为网络架构中的重要组成部分，并随着技术的进步和需求的变化不断发展和完善')


def page_4():
    '''我的留言区'''
    st.write('我的留言区')
    # 从文件中加载内容，并处理成列表
    with open('leave_messages.txt', 'r', encoding='utf-8') as f:
        messages_list = f.read().split('\n')
    for i in range(len(messages_list)):
        messages_list[i] = messages_list[i].split('#')
    for i in messages_list:
        if i[1] == '阿短':
            with st.chat_message('🌞'):
                st.write(i[1],':',i[2])
        elif i[1] == '编程猫':
            with st.chat_message('🍥'):
                st.write(i[1],':',i[2])
    name = st.selectbox('我是……', ['阿短', '编程猫'])
    new_message = st.text_input('想要说的话……')
    if st.button('留言'):
        messages_list.append([str(int(messages_list[-1][0])+1), name, new_message])
        with open('leave_messages.txt', 'w', encoding='utf-8') as f:
            message = ''
            for i in messages_list:
                message += i[0] + '#' + i[1] + '#' + i[2] + '\n'
            message = message[:-1]
            f.write(message)

    # 跳转按钮link_button()
    st.link_button('百度首页', 'https://www.baidu.com/')
    
    # 如何创建跳转按钮
    # 普通的按钮需要编写if判断触发效果，跳转按钮需要吗？
    
    st.write('其他网站')
    st.write('除了本主站之外，我还将我的有趣内容分享在了其他网站中')
    go = st.selectbox('你的支持是我最大的动力，去支持一下up吧！', ['我的贴吧', '我的bilibili'])
    if go == '我的贴吧':
        st.link_button('帮我盖楼', 'https://www.baidu.com/')
    elif go == '我的bilibili':
        st.link_button('帮我一键三连', 'https://www.bilibili.com/')


def img_change(img, rc, gc, bc):
    '''图片处理'''
    width, height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            # 获取RGB值
            r = img_array[x, y][rc]
            g = img_array[x, y][gc]
            b = img_array[x, y][bc]
            img_array[x, y] = (r, g, b)
    return img

if page == '我的兴趣推荐':
    page_1()
elif page == '我的图片处理工具':
    page_2()
elif page == '我的智慧词典':
    page_3()
elif page == '我的留言区':
    page_4()