# 个人收支记账小工具（Python入门版）
def main():
    """主函数：程序入口，控制整体流程"""
    # 1. 初始化数据：用列表存储收支记录，每个元素是字典（键值对存储金额、类型、备注）
    records = []
    # 2. 欢迎语
    print("🎉 欢迎使用新手入门版收支记账工具 🎉")
    print("操作说明：1-记录收入 | 2-记录支出 | 3-查看记录 | 4-查看余额 | 0-退出\n")

    # 3. 循环操作（直到用户选择退出）
    while True:
        # 获取用户操作选择
        try:
            choice = int(input("请输入操作编号（0-4）："))
        except ValueError:
            print("❌ 错误：请输入数字（0-4）！\n")
            continue

        # 4. 条件判断：处理不同操作
        if choice == 0:
            # 退出程序
            print("\n👋 感谢使用，再见！")
            break
        elif choice == 1:
            # 记录收入
            record_income(records)
        elif choice == 2:
            # 记录支出
            record_expense(records)
        elif choice == 3:
            # 查看所有记录
            show_records(records)
        elif choice == 4:
            # 计算并查看余额
            show_balance(records)
        else:
            print("❌ 错误：请输入有效的操作编号（0-4）！\n")

def record_income(records):
    """记录收入的函数"""
    try:
        amount = float(input("请输入收入金额："))
        if amount <= 0:
            print("❌ 收入金额必须大于0！\n")
            return
        remark = input("请输入收入备注（如：工资、兼职）：")
        # 向列表添加收入记录（字典格式）
        records.append({"type": "收入", "amount": amount, "remark": remark})
        print(f"✅ 收入 {amount} 元记录成功！\n")
    except ValueError:
        print("❌ 金额必须是数字（如100、50.5）！\n")

def record_expense(records):
    """记录支出的函数"""
    try:
        amount = float(input("请输入支出金额："))
        if amount <= 0:
            print("❌ 支出金额必须大于0！\n")
            return
        remark = input("请输入支出备注（如：吃饭、购物）：")
        # 向列表添加支出记录（字典格式）
        records.append({"type": "支出", "amount": amount, "remark": remark})
        print(f"✅ 支出 {amount} 元记录成功！\n")
    except ValueError:
        print("❌ 金额必须是数字（如50、20.8）！\n")

def show_records(records):
    """查看所有收支记录"""
    if not records:
        print("📝 暂无收支记录！\n")
        return
    print("\n📜 所有收支记录：")
    print("-" * 50)
    # 遍历记录列表，打印每条记录
    for i, record in enumerate(records, 1):  # enumerate：带索引遍历，从1开始计数
        print(f"{i}. {record['type']} | 金额：{record['amount']} 元 | 备注：{record['remark']}")
    print("-" * 50 + "\n")

def show_balance(records):
    """计算并显示余额"""
    income_total = 0  # 总收入
    expense_total = 0 # 总支出
    # 遍历记录，累加收入和支出
    for record in records:
        if record["type"] == "收入":
            income_total += record["amount"]
        else:
            expense_total += record["amount"]
    balance = income_total - expense_total  # 余额=收入-支出
    print("\n💰 账户余额：")
    print(f"总收入：{income_total} 元 | 总支出：{expense_total} 元 | 当前余额：{balance} 元\n")

# 运行主函数
if __name__ == "__main__":
    main()