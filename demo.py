import tkinter as tk
import random
import math
import sys

# 创建主窗口
root = tk.Tk()
root.withdraw()

# 弹窗文本列表
popup_messages = [
    "你好！",
    "今天天气真好！",
    "祝你心情愉快！",
    "工作顺利！",
    "身体健康！",
    "天天开心！",
    "心想事成！",
    "好运连连！",
]

# 弹窗背景色列表
popup_colors = [
    "#FFB6C1",  # 浅粉色
    "#FFC0CB",  # 粉红色
    "#FF69B4",  # 热粉色
    "#FF1493",  # 深粉色
    "#FFB3BA",  # 粉红色
    "#FFDFD3",  # 浅粉色
    "#FFA07A",  # 浅鲑鱼色
    "#FFE4E1",  # 淡粉色
]

# 生成爱心形状的点位列表
def generate_heart_positions(screen_width, screen_height, window_width, window_height, num_points=25):
    """
    生成爱心形状的点位列表
    使用参数方程: x = 16sin³(t), y = 13cos(t) - 5cos(2t) - 2cos(3t) - cos(4t)
    增大尺寸并确保居中
    """
    positions = []
    # 爱心的大小系数（增大尺寸，让爱心更大）
    scale = min(screen_width, screen_height) / 2.5  # 从/5改为/2.5，让爱心更大
    # 中心点（确保居中）
    center_x = screen_width // 2
    center_y = screen_height // 2
    
    for i in range(num_points):
        t = 2 * math.pi * i / num_points
        # 爱心参数方程
        x_param = 16 * (math.sin(t) ** 3)
        y_param = 13 * math.cos(t) - 5 * math.cos(2*t) - 2 * math.cos(3*t) - math.cos(4*t)
        
        # 转换为屏幕坐标（注意y需要翻转，并且要减去窗口尺寸的一半以确保窗口中心在爱心上）
        x = int(center_x + x_param * scale / 16 - window_width / 2)
        y = int(center_y - y_param * scale / 13 - window_height / 2)  # 翻转y轴
        
        # 确保窗口在屏幕内
        x = max(0, min(x, screen_width - window_width))
        y = max(0, min(y, screen_height - window_height))
        
        positions.append((x, y))
    
    return positions

# 弹窗计数器
popup_count = 0
# 当前打开的弹窗数量
active_popups = 0
# 爱心点位列表（稍后初始化）
heart_positions = []
# 爱心弹窗是否全部显示完毕
heart_complete = False
# 屏幕尺寸和窗口尺寸（全局）
screen_width = 0
screen_height = 0
window_width = 300
window_height = 100

# 创建一个自定义弹窗（带3秒自动关闭和倒计时）
def show_pink_popup():
    global active_popups, popup_count, heart_positions, screen_width, screen_height, window_width, window_height
    
    # 增加打开的弹窗计数
    active_popups += 1
    
    # 随机选择文本和背景色
    message = random.choice(popup_messages)
    bg_color = random.choice(popup_colors)
    
    # 创建新的顶层窗口
    popup = tk.Toplevel(root)
    popup.title("提示")
    popup.geometry("300x100")
    popup.configure(bg=bg_color)  # 随机背景色
    
    # 初始化爱心点位列表（如果还没有）
    if not heart_positions:
        heart_positions = generate_heart_positions(screen_width, screen_height, window_width, window_height)
    
    # 从爱心点位列表中选择目标位置（循环使用）
    # 注意：这里使用popup_count作为索引（在第一个弹窗时popup_count=0）
    position_index = popup_count % len(heart_positions)
    target_x, target_y = heart_positions[position_index]
    
    # 随机生成起始位置
    start_x = random.randint(0, max(0, screen_width - window_width))
    start_y = random.randint(0, max(0, screen_height - window_height))
    
    # 先在随机位置显示窗口
    popup.geometry(f"{window_width}x{window_height}+{start_x}+{start_y}")
    
    # 移动动画参数
    current_x = start_x
    current_y = start_y
    animation_steps = 30  # 动画步数
    step_x = (target_x - start_x) / animation_steps
    step_y = (target_y - start_y) / animation_steps
    step_count = 0
    
    # 移动动画函数
    def animate_move():
        nonlocal current_x, current_y, step_count
        if step_count < animation_steps and popup.winfo_exists():
            current_x += step_x
            current_y += step_y
            popup.geometry(f"{window_width}x{window_height}+{int(current_x)}+{int(current_y)}")
            step_count += 1
            popup.after(16, animate_move)  # 约60fps的动画
    
    # 开始移动动画
    popup.after(50, animate_move)
    
    # 添加提示文本（不显示倒计时）
    label = tk.Label(
        popup,
        text=message,
        bg=bg_color,  # 随机背景色
        fg="#000000",  # 黑色文字
        font=("Arial", 16, "bold"),
        pady=30
    )
    label.pack()
    
    # 爱心弹窗不关闭，保持在爱心位置上
    # 不需要倒计时和关闭逻辑

# 从中心向四周发射的弹窗函数
def show_center_popup():
    global active_popups, screen_width, screen_height
    
    # 增加打开的弹窗计数
    active_popups += 1
    
    # 随机选择文本和背景色
    message = random.choice(popup_messages)
    bg_color = random.choice(popup_colors)
    
    # 创建新的顶层窗口
    popup = tk.Toplevel(root)
    popup.title("提示")
    
    # 初始窗口尺寸
    initial_width = 300
    initial_height = 100
    
    # 中心位置
    center_x = screen_width // 2
    center_y = screen_height // 2
    
    # 随机选择方向（8个方向：上、下、左、右、左上、右上、左下、右下）
    angle = random.uniform(0, 2 * math.pi)
    
    # 计算目标位置（移动到屏幕边缘附近）
    max_distance = min(screen_width, screen_height) // 2
    target_x = int(center_x + math.cos(angle) * max_distance)
    target_y = int(center_y + math.sin(angle) * max_distance)
    
    # 确保在屏幕内
    target_x = max(0, min(target_x, screen_width - initial_width))
    target_y = max(0, min(target_y, screen_height - initial_height))
    
    # 在中心位置显示窗口
    popup.geometry(f"{initial_width}x{initial_height}+{center_x - initial_width//2}+{center_y - initial_height//2}")
    popup.configure(bg=bg_color)
    
    # 添加提示文本
    label = tk.Label(
        popup,
        text=message,
        bg=bg_color,
        fg="#000000",
        font=("Arial", 16, "bold"),
        pady=30
    )
    label.pack()
    
    # 动画参数
    current_x = center_x - initial_width // 2
    current_y = center_y - initial_height // 2
    current_width = initial_width
    current_height = initial_height
    animation_duration = 3000  # 3秒
    animation_steps = 180  # 约60fps * 3秒
    elapsed_steps = 0
    
    step_x = (target_x - current_x) / animation_steps
    step_y = (target_y - current_y) / animation_steps
    shrink_width = current_width / animation_steps
    shrink_height = current_height / animation_steps
    
    # 移动和缩小动画函数
    def animate():
        nonlocal current_x, current_y, current_width, current_height, elapsed_steps
        if elapsed_steps < animation_steps and popup.winfo_exists():
            current_x += step_x
            current_y += step_y
            current_width -= shrink_width
            current_height -= shrink_height
            
            # 确保尺寸不为负
            w = max(10, int(current_width))
            h = max(10, int(current_height))
            
            popup.geometry(f"{w}x{h}+{int(current_x)}+{int(current_y)}")
            
            # 更新标签字体大小（随窗口缩小）
            font_size = max(8, int(16 * (current_width / initial_width)))
            label.config(font=("Arial", font_size, "bold"))
            
            elapsed_steps += 1
            popup.after(16, animate)  # 约60fps
        else:
            # 动画结束，关闭弹窗
            close_popup()
    
    # 关闭弹窗的函数
    def close_popup():
        global active_popups
        if popup.winfo_exists():
            popup.destroy()
        active_popups -= 1
    
    # 绑定窗口关闭事件
    popup.protocol("WM_DELETE_WINDOW", close_popup)
    
    # 开始动画
    popup.after(50, animate)

# 定时创建弹窗的函数
def create_next_popup():
    global popup_count, heart_positions, heart_complete
    show_pink_popup()
    popup_count += 1
    # 弹窗数量等于爱心点位数量，围成一个完整的爱心
    if popup_count < len(heart_positions):
        # 0.5秒后创建下一个弹窗
        root.after(500, create_next_popup)
    else:
        # 爱心弹窗全部显示完毕
        heart_complete = True
        # 开始从中心向四周发射弹窗
        start_center_popups()

# 从中心持续发射弹窗的函数
def start_center_popups():
    """从中心持续向四周发射弹窗"""
    if heart_complete:
        show_center_popup()
        # 每0.3秒创建一个新弹窗，持续循环
        root.after(300, start_center_popups)

# 创建停止按钮（在左下角）
def create_stop_button():
    """在屏幕左下角创建停止按钮"""
    stop_window = tk.Toplevel(root)
    stop_window.title("控制")
    stop_window.geometry("120x50")
    stop_window.attributes('-topmost', True)  # 置顶显示
    
    # 获取屏幕尺寸，将按钮放在左下角
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    stop_window.geometry(f"120x50+10+{screen_height - 70}")
    
    # 移除窗口装饰（可选，但保留会更好）
    # stop_window.overrideredirect(True)
    
    # 创建停止按钮
    def stop_program():
        """停止程序"""
        global active_popups, heart_complete
        
        # 停止创建新弹窗
        heart_complete = False
        
        # 关闭所有弹窗（包括stop_window本身）
        # 获取所有顶层窗口
        toplevels = []
        for widget in root.winfo_children():
            if isinstance(widget, tk.Toplevel):
                toplevels.append(widget)
        
        # 关闭所有顶层窗口
        for window in toplevels:
            try:
                window.destroy()
            except:
                pass
        
        # 退出程序
        try:
            root.quit()
            root.destroy()
        except:
            sys.exit(0)
    
    stop_button = tk.Button(
        stop_window,
        text="停止",
        command=stop_program,
        bg="#FF6B6B",
        fg="#FFFFFF",
        font=("Arial", 14, "bold"),
        padx=20,
        pady=10,
        relief="raised",
        bd=3
    )
    stop_button.pack(expand=True, fill=tk.BOTH)
    
    return stop_window

# 初始化全局变量
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width = 300
window_height = 100
heart_positions = generate_heart_positions(screen_width, screen_height, window_width, window_height)

# 创建停止按钮（在左下角）
create_stop_button()

# 立即显示第一个弹窗
show_pink_popup()
popup_count = 1

# 0.5秒后创建下一个弹窗
root.after(500, create_next_popup)

# 运行主循环
root.mainloop()

