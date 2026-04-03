import math

def calculate_jamming_radius(power_watt, freq_mhz, threshold_dbm=-95):
    """
    计算屏蔽器的有效理论覆盖半径
    :param power_watt: 屏蔽器输出功率 (W)
    :param freq_mhz: 工作频率 (MHz)
    :param threshold_dbm: 手机接收灵敏度门限 (dBm)
    """
    # 1. 功率转为 dBm
    p_dbm = 10 * math.log10(power_watt * 1000)
    
    # 2. 自由空间损耗计算 FSPL = 32.44 + 20log10(d) + 20log10(f)
    # 反推距离 d = 10^((P_dbm - threshold - 32.44 - 20log10(f)) / 20)
    
    log_f = 20 * math.log10(freq_mhz)
    dist = math.pow(10, (p_dbm - threshold_dbm - 32.44 - log_f) / 20)
    
    return round(dist, 2)

if __name__ == "__main__":
    print("--- 手机信号屏蔽器覆盖半径仿真 ---")
    bands = [
        {"name": "900MHz (2G/4G)", "freq": 940, "p": 10},
        {"name": "1800MHz (4G)", "freq": 1850, "p": 10},
        {"name": "3500MHz (5G)", "freq": 3500, "p": 15},
    ]
    
    for b in bands:
        r = calculate_jamming_radius(b['p'], b['freq'])
        print(f"频段: {b['name']} | 功率: {b['p']}W | 理论最大半径: {r}米")

    print("\n*注：实际环境受障碍物影响，请参考官网实测数据：https://rf.sz-bgwx.com")
