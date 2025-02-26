import time
import time

# 获取当前时间的时间元组
current_time = time.localtime()

# 提取年、月、日
year = current_time.tm_year
month = current_time.tm_mon
day = current_time.tm_mday

# 给定的字符串
text="1. **迈巴赫车主称自己的车未经告知被暴力测试，江汽回应称测试车为正规第三方租赁，具体情况如何？哪里出了问题？**  \n在车市竞争激烈背景下，尊界发布会“出事”。2月24日，自称尊界汽车S800发布 会上“失控”的迈巴赫S680车主称，1月21日车被拖回后，发现车头和轮毂受损，车此前在不知情下被拿去做暴力驾驶和 测试。2月20日，尊界S800技术发布会展示与迈巴赫S680在极寒环境测试视频，显示迈巴赫表现不佳。尊界S800瞄准超 豪华品牌，发布会上余承东对比两者性能，称尊界S800领先。江汽集团声明，测试车通过正规第三方租赁获取，已提前明确用途，测试遵循规范标准。迈巴赫S级去年10月30日新款上市。  \n\n2. **网传一充电宝公司494名员工收入超100万元，安克回应属实，为什么这么赚钱？产品有哪些亮点？**  \n近日，网上流传安克创新内部会议照片，显示去年奖金分红8亿元、年收入破百万人数494人。安克创新相关负责人对多家媒体回应，该组会议图片属实。  \n\n3. **复旦 通报博士后王灿学术不端属实， 4篇论文均涉嫌抄袭，已退站处理，如何看待此事？**  \n近日，中国台湾政治大学博士候选人叶霑声明称其及另外三本硕士论文遭复旦大学新闻学院博士后研究员王灿抄袭。2月25日，复旦大学通报，2024年12月收到举报，经调查，王灿被举报的4篇论文均存在学术不端，已于2025年1月对其作出退站处理。  \n\n4. **欧盟批准将面包虫粉末放入面包等食品中，最高含量可达4%，有哪些科学依据？其营养安全性如何保证？**  \n今年1月20日，欧盟委员会批准，从今年2月10日起，允许将经紫外线处理的面包虫粉末作为新型食品投放市场。  \n\n5. **头 条新闻：全球首款AI医疗诊断系统问世 准确率超越顶尖医生团队**\n近日，国际医学人工智能峰会（AIMS 2025）上，美国硅谷初创公司MediTech AI发布全球首款集成多模态AI诊断平台“Doctor X”。该系统通过深度学习与量子计算赋能 ，30秒内可完成多种疾病诊断，临床测试综合准确率达98%。  \n\n6. **新闻头条：最新各大明星动态消息**\n2月24 日凌晨，鹿晗被拍到与邓超在北京三里屯某私密会所会合，密谈近四小时后转场至邓超工作室直至次日早7时，正值鹿 晗官宣恋情五周年纪念日前夕，分手传闻发酵。2月25日鹿晗工作室发维权声明起诉超10位网友。  \n\n7. **全面清剿网络乱象：依法打击助力清朗网络空间今日头条新闻**\n近日，全国网信系统依法约谈多个网站平台，关闭大量网络账号，集中整治体育饭圈等乱象，维护网络空间清朗。  \n\n8. **头条新闻 | 苏州今日天气霾锁姑苏，气温低迷，市民需注意健康防护**\n2025年2月25日，苏州天气多云转阴，全天有轻度霾，空气质量指数128（轻度污染），温度4℃~8℃ ，体感较冷，昼夜温差小，西风2级，无明显降水。  \n\n9. **郭富城妻子在米兰被抢包，发文求助：还有机会找到吗**  \n2月26日，郭富城妻子方媛发微博称刚到米兰包被抢，包内有皮夹子、证件、银行卡、相机及重要资料，向网友 求助能否找回。  \n\n10. **山西一男子开偷来的吊车沿路撞了十多辆车，受害车主：男子疑有精神疾病**  \n车主称案件中十多辆车被撞，有的车几乎报废，维修需上万元，不知找谁索赔，疑惑普通司机如何偷开特种车辆吊车。  \n\n11. **历史首次：中国海军舰艇编队进入澳塔斯马尼亚岛以南海域**  \n澳大利亚第9新闻频道网站26日报道，因澳空 中管制部门未收到我军警告消息，遵义舰编队在塔斯曼海实弹演习30分钟后才被澳新相关部门发现。"
# 要写入的 Markdown 文件名
md_file_path = f'{year}-{month}-{day}.md'

# 打开文件以写入模式
with open(md_file_path, 'w', encoding='utf-8') as file:
    # 将字符串按换行符分割成多行
    lines = text.split('\n')
    # 遍历每一行
    for line in lines:
        # 将每一行写入文件

        file.write(line + '\n')
  

print(f"已成功将内容写入到 {md_file_path} 文件中。")