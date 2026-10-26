# 2026-10-26 外部链接异常复核

结论：56 个“访问异常”不是 56 个失效数据集。它们混合了取数入口、历史材料、论文来源、API 起点和同一主机的 URL 变体。本轮修正了有官方证据的新申请路径，并保留未确认的服务故障；没有为了降低报错数删来源、替换数据身份或提升记录状态。

## 这份报告对应哪次检查

原运行 [40309000568](https://github.com/mimaowang/Econ-DataKnowhow/actions/runs/40309000568) 的日志留下总数 56，逐项清单只在需登录的 summary 中，当前连接未取回，所以不能声称重建了原始 56 项的确切成员。为此只增加了将既有 JSON 打印进日志的操作，再对同一代码版本的同一 150-URL 取样范围复扫。

本表逐项对应可读明细的 [40311414672](https://github.com/mimaowang/Econ-DataKnowhow/actions/runs/40311414672)，检查时间为 2026-10-26 11:02:40 UTC，提交为 `8bc8eef22549f886d39967d94240cc23098fb23d`。共 932 个唯一 URL，检查前 150 个，仍有 56 个异常；相同总数不证明前后成员完全相同。这不是全库 932 个 URL 的完整网络审计。

原始结果为：403 ×24、404 ×4、400 ×1、422 ×1、429 ×1、521 ×2、DNS 失败 ×11、超时 ×5、连接直接关闭 ×2、其他网络失败 ×3、TLS 失败 ×2。普通浏览器能打开多个原址，说明不能把这些状态码直接变成“数据不可用”。网页读取器有时自动把 HTTP 换成 HTTPS，读取器失败也不等于浏览器访问原址失败。

## 会改变研究者下一步的修正

CGSS 和 CLASS 的官网已正式链接人民大学 CSSD 平台。两份指南现在从对应数据空间开始，说明认证、协议和逐文件权限；CLASS 还需要邮件注明 CSSD 用户名和波次。CHFS 的旧数据中心确实 404，已改到官网正式链接的申请平台，保留 2011-2021 一般申请与 2023/2025 尚未一般开放的区别。

CRRS 的网页本身能打开，但内容揭示了更严重的旧流程问题：2025 年说明已关闭邮件申请，改为国内申请者获批后在云桌面使用 2020/2022 数据、审核后导出研究结果。现已同步修正，不再承诺邮件取得原始微观文件。此项是既有农业记录的必要维护，不是扩大农业收集范围。CHIP 官方说明仍在，但申请门户出现部署侧 502，已注明中断，并保留仅覆盖 2002 的独立 ICPSR 路线。UCSB 旧论文 PDF 确认 404，已标明文档路线待复核，独立作者复现页和历史阅读证据保留。

下面的“可读”仅指所列页面或索引正文，不证明账号获批、微观文件已下载、全部年份可得或论文最终分析文件可复现。本轮没有登录申请、提交身份材料、绕过证书/验证码、削弱网络校验或删除任何文件。发布门禁结果以对应 PR 检查为准。

## 56 项逐项结果

| # | 原 URL | 关联记录 | 扫描结果 | 复核与处理 |
| --- | --- | --- | --- | --- |
| 1 | <http://caser.ust.hk/?act=hkpssd_data> | [china-hkpssd-geocoded-survey-2026](../datasets/china-hkpssd-geocoded-survey-2026.md) | URLError | **未确认**：HKUST 旧 HKPSSD 入口超时；网页读取器亦未取得内容。 保留历史入口；联系项目或核对 NYU Shanghai 官方项目页，不能据此承诺微观地理数据可申请。 |
| 2 | <http://chip.bnu.edu.cn/> | [chip](../datasets/chip.md), [uhs](../datasets/uhs.md) | RemoteDisconnected | **服务异常**：浏览器跟随官网跳转后出现部署侧 502；北师大官方申请说明仍链接该门户。 已在 CHIP 和 UHS 的 CHIP 替代路线中注明中断。ICPSR 21741 仅是 CHIP 2002 的独立路线。 |
| 3 | <http://cnsda.ruc.edu.cn> | [cgss](../datasets/cgss.md) | URLError | **官方新路线**：旧 CNSDA 地址在扫描中 DNS 失败，浏览器为空响应；CGSS 官网正式链接 CSSD。 CGSS 已改用 https://cssd.ruc.edu.cn/dataspace/cgss；旧链接作为历史来源保留。 |
| 4 | <http://cnsda.ruc.edu.cn/> | [cgss](../datasets/cgss.md), [class-china-longitudinal-aging-social-survey](../datasets/class-china-longitudinal-aging-social-survey.md) | URLError | **官方新路线**：同一旧 CNSDA 主机的尾斜杠变体，不是第二个独立数据源；CLASS 也有正式 CSSD 数据空间。 CLASS 改用 https://cssd.ruc.edu.cn/dataspace/CLASS，保留签署协议、邮件注明用户名/波次、逐文件审核步骤。 |
| 5 | <http://css.cssn.cn/> | [css-chinese-social-survey](../datasets/css-chinese-social-survey.md) | 403 | **浏览器可读**：原 HTTP 首页在普通浏览器跳转到 /css_sy/ 并正常显示调查网站。 不换域名、不判定数据消失；GitHub HEAD 403 是客户端访问差异。 |
| 6 | <http://css.cssn.cn/css_sy/zlysj/lnsj/> | [css-chinese-social-survey](../datasets/css-chinese-social-survey.md) | 403 | **浏览器可读**：原历年数据目录能打开，列出波次和数据申请说明。 保留；目录可读不等于已获微观数据下载权限。 |
| 7 | <http://css.cssn.cn/css_sy/zlysj/lnsj/202209/t20220926_5541891.html> | [css-chinese-social-survey](../datasets/css-chinese-social-survey.md) | 403 | **未确认**：目录能列出这篇说明，但本文在浏览器及网页读取器中未完成加载。 保留并待合法浏览器/机构网络复核正文；不根据目录链接存在宣称本文已读。 |
| 8 | <http://data.court.gov.cn/pages/research.html> | [china-court-judgments-2014-2018-open-justice](../datasets/china-court-judgments-2014-2018-open-justice.md) | URLError | **服务异常**：GitHub DNS 失败，浏览器原地址为空响应。 保留历史研究平台证据；现有论文数据与公开裁判文书不是同一可下载产品，不猜新接口。 |
| 9 | <http://gi.mnr.gov.cn/202402/P020240312701247258838.pdf> | [mnr-national-real-estate-registration-bulletins](../datasets/mnr-national-real-estate-registration-bulletins.md), [mnr-real-estate-registration](../datasets/mnr-real-estate-registration.md) | URLError | **附件未确认**：2023 公报官方文章可读，仍列出这个 PDF 附件；读取器未取得附件。 保留原附件，优先从对应官方文章进入；没有验证 PDF 文件下载。 |
| 10 | <http://gi.mnr.gov.cn/202402/t20240229_2838490.html> | [mnr-real-estate-registration](../datasets/mnr-real-estate-registration.md) | URLError | **浏览器可读**：原地址正常跳转 HTTPS 同路径，显示自然资源部 2023 年公报及对应附件。 不把 GitHub DNS 失败解释为站点退役；无需替换。 |
| 11 | <http://gi.mnr.gov.cn/202503/P020251209353094119242.pdf> | [mnr-national-real-estate-registration-bulletins](../datasets/mnr-national-real-estate-registration-bulletins.md), [mnr-real-estate-registration](../datasets/mnr-real-estate-registration.md) | URLError | **附件未确认**：2024 公报官方文章可读，仍列出这个精确 PDF；读取器未取得附件。 保留原附件及官方文章；文件下载仍未验证。 |
| 12 | <http://gi.mnr.gov.cn/202503/t20250314_2881937.html> | [mnr-real-estate-registration](../datasets/mnr-real-estate-registration.md) | URLError | **浏览器可读**：原地址跳转 HTTPS 同路径，显示 2024 年公报、官方索引号及附件。 保留；本次不是整份公报内容审计。 |
| 13 | <http://lib.nufe.edu.cn/2024/1010/c438a9020/page.htm> | [resset](../datasets/resset.md) | 403 | **受工具限制**：扫描 403；浏览器复核被导航策略阻止，未取得独立页面证据。 保留 RESSET 的机构说明来源，暂不改写可得性；未用其他客户端绕过限制。 |
| 14 | <http://m.bj.bendibao.com/news/gelizhengce/fengxianmingdan.php> | [china-county-daily-covid-risk-level-2020-2022](../datasets/china-county-daily-covid-risk-level-2020-2022.md) | 404 | **历史页面 404**：GitHub 原 URL 返回 404；该记录本来就说明它是 2022 年历史备用风险名单页面。 不将其作为当前取数入口；保留历史来源。作者发布的数据文件是另一路线。 |
| 15 | <http://opac.sdtbu.edu.cn/opac/show_format_marc.php?marc_no=0f6e5263503153640e635167016652330e355633> | [china-agricultural-census-1997-1pct](../datasets/china-agricultural-census-1997-1pct.md) | URLError | **未确认**：旧 OPAC MARC 链接超时，读取器未取得内容。 这是馆藏目录证据，不是农业普查微观数据下载；不据此删记录或扩大农业收集。 |
| 16 | <http://rdi.cssn.cn/> | [crrs-rural-revitalization-survey](../datasets/crrs-rural-revitalization-survey.md) | 403 | **浏览器可读**：RDI 官方首页可读。 保留；与数据访问方式分开判断。 |
| 17 | <http://rdi.cssn.cn/dcsj/> | [crrs-rural-revitalization-survey](../datasets/crrs-rural-revitalization-survey.md) | 403 | **浏览器可读**：调查数据目录可读，列出第一、二期公告。 保留官方目录。 |
| 18 | <http://rdi.cssn.cn/dcsj/202306/t20230607_5643271.shtml> | [crrs-rural-revitalization-survey](../datasets/crrs-rural-revitalization-survey.md) | 403 | **浏览器可读／旧流程**：旧第一期说明可读，但其中邮件申请已经被新版说明取代。 保留历史证据，不再用它指导当前申请。 |
| 19 | <http://rdi.cssn.cn/dcsj/202504/t20250429_5871894.shtml> | [crrs-rural-revitalization-survey](../datasets/crrs-rural-revitalization-survey.md) | 403 | **浏览器可读／实质修复**：2025-04-29 公告可读，明确关闭邮件申请，改为 2020/2022 云桌面使用、审核后导出结果。 已同步修正 CRRS 的当前路线、交付物、资格、排队/抽签及正文；未测试云端登录或提交证件。 |
| 20 | <http://rkyj.ruc.edu.cn> | [china-2017-fertility-survey](../datasets/china-2017-fertility-survey.md) | 403 | **浏览器可读**：原域名跳转到 https://rkyj.ruc.edu.cn/CN/1000-6087/home.shtml，正常显示《人口研究》。 期刊网站而非调查微观数据下载站；保留论文来源角色。 |
| 21 | <http://rst.gxzf.gov.cn/zwgk/xxgkzcfg/xxgkwjjd/tw/t3254177.shtml> | [china-minimum-wage-policy-panel](../datasets/china-minimum-wage-policy-panel.md) | TimeoutError | **未确认**：GitHub 超时；网页读取器的 HTTPS 请求返回 502。 保留广西政策历史出处；未证实新址，不将读取器故障直接算作永久失效。 |
| 22 | <http://swj.trs.gov.cn/ztzl/dzswjnc/201903/t20190306_21835611.html> | [china-mofcom-rural-ecommerce-demo-counties](../datasets/china-mofcom-rural-ecommerce-demo-counties.md) | URLError | **未确认**：GitHub 网络不可达；读取器也未取得正文。 保留地方商务历史通知来源，待合法原站/正式转载核实。 |
| 23 | <http://szzdjc.cnemc.cn:8070/GJZ/Business/Publish/Main.html> | [china-water-quality-monitoring](../datasets/china-water-quality-monitoring.md) | URLError | **未确认**：带 8070 端口的水质发布页面超时；读取器不支持此次请求。 保留精确原址，未来从 CNEMC 官网核对当前发布入口；没有关闭网络校验或猜接口。 |
| 24 | <http://www.baobeihuijia.com> | [china-trafficked-children-inflow](../datasets/china-trafficked-children-inflow.md) | 521 | **服务异常**：GitHub 返回 521，独立网页读取也返回 521。 作为源站服务异常保留；网页打不开不证明论文历史样本消失，也不构成重建授权。 |
| 25 | <http://www.card.zju.edu.cn/2026/0318/c24473a3141956/page.htm> | [charls](../datasets/charls.md) | 403 | **受工具限制**：扫描 403；浏览器复核受导航策略阻止。 这是 CHARLS 的机构介绍证据，不据此改写 CHARLS 官方申请路线。 |
| 26 | <http://www.gzxy.gov.cn/gzxysite/xysrsj/1342/202608/t20260812_90724419.html> | [china-minimum-wage-policy-panel](../datasets/china-minimum-wage-policy-panel.md) | URLError | **未确认**：GitHub 网络不可达；读取器也未取得正文。 保留地方最低工资历史通知，不猜替换地址。 |
| 27 | <http://www.kman.gov.cn/c/2025-01-06/6955078.shtml> | [china-5a-scenic-area-list](../datasets/china-5a-scenic-area-list.md) | RemoteDisconnected | **未确认**：GitHub 断开连接；读取器超时。 保留 5A 名单的地方出处；国家正式公告与地方转述各自保留角色。 |
| 28 | <http://www.moa.gov.cn/gk/yjgl_l/> | [china-weekly-provincial-hog-prices](../datasets/china-weekly-provincial-hog-prices.md) | 404 | **旧目录 404**：扫描对 MOA 旧目录返回 404；读取器未能独立取回该页。 旧目录不是论文最终猪价面板；官方畜牧兽医局目录可作后续发现线索，但尚未证明旧历史栏目无损迁移，不直接替换。 |
| 29 | <http://www.sres.org.cn> | [china-io-table](../datasets/china-io-table.md) | URLError | **服务异常**：旧 SRES 主机 GitHub DNS 失败，浏览器空响应。 保留投入产出数据生产来源；没有证据证明另一网站是同一机构/同一数据交付的继任者。 |
| 30 | <http://www.sres.org.cn/> | [china-io-table](../datasets/china-io-table.md) | URLError | **服务异常**：与上一行同一 SRES 主机的尾斜杠变体。 按同一故障处理，不计成两个数据集消失。 |
| 31 | <https://academic.oup.com/joeg/advance-article-abstract/doi/10.1093/jeg/lbaf059/8382698> | [china-land-transaction](../datasets/china-land-transaction.md) | 403 | **出版方拒绝自动访问**：同一 Oxford 主机的扫描为 403；本轮没有逐篇绕过验证读取正文，不能确认各页内容。 保留论文证据地址，不完成挑战、不改用未核实的镜像，也不据此降低其关联数据资产的成熟度。 |
| 32 | <https://academic.oup.com/joeg/article/25/2/151/7725676> | [asif](../datasets/asif.md), [china-land-transaction](../datasets/china-land-transaction.md) | 403 | **出版方拒绝自动访问**：同一 Oxford 主机的扫描为 403；本轮没有逐篇绕过验证读取正文，不能确认各页内容。 保留论文证据地址，不完成挑战、不改用未核实的镜像，也不据此降低其关联数据资产的成熟度。 |
| 33 | <https://academic.oup.com/psychsocgerontology/article/79/7/gbae081/7671273> | [class-china-longitudinal-aging-social-survey](../datasets/class-china-longitudinal-aging-social-survey.md) | 403 | **出版方拒绝自动访问**：同一 Oxford 主机的扫描为 403；本轮没有逐篇绕过验证读取正文，不能确认各页内容。 保留论文证据地址，不完成挑战、不改用未核实的镜像，也不据此降低其关联数据资产的成熟度。 |
| 34 | <https://academic.oup.com/qje/article-abstract/113/3/773/1851137> | [china-agricultural-yearbook](../datasets/china-agricultural-yearbook.md), [china-domestic-trade-statistical-yearbook](../datasets/china-domestic-trade-statistical-yearbook.md), [china-industrial-commerce-administration-statistics-40-years](../datasets/china-industrial-commerce-administration-statistics-40-years.md), [china-rural-finance-statistical-yearbook](../datasets/china-rural-finance-statistical-yearbook.md), [china-stat-yearbook](../datasets/china-stat-yearbook.md), [china-township-enterprises-statistical-material-1978-1985](../datasets/china-township-enterprises-statistical-material-1978-1985.md), [china-township-enterprises-statistical-yearbook](../datasets/china-township-enterprises-statistical-yearbook.md) | 403 | **出版方拒绝自动访问**：该精确论文页在浏览器显示 Cloudflare 安全验证，扫描为 403。 保留论文证据地址，不完成挑战、不改用未核实的镜像，也不据此降低其关联数据资产的成熟度。 |
| 35 | <https://academic.oup.com/qje/article-abstract/123/3/1251/1928174> | [china-census](../datasets/china-census.md) | 403 | **出版方拒绝自动访问**：同一 Oxford 主机的扫描为 403；本轮没有逐篇绕过验证读取正文，不能确认各页内容。 保留论文证据地址，不完成挑战、不改用未核实的镜像，也不据此降低其关联数据资产的成熟度。 |
| 36 | <https://academic.oup.com/qje/article-abstract/128/1/287/1839620?login=false> | [china-zhaopin-job-ads-2008-2010](../datasets/china-zhaopin-job-ads-2008-2010.md) | 403 | **出版方拒绝自动访问**：同一 Oxford 主机的扫描为 403；本轮没有逐篇绕过验证读取正文，不能确认各页内容。 保留论文证据地址，不完成挑战、不改用未核实的镜像，也不据此降低其关联数据资产的成熟度。 |
| 37 | <https://academic.oup.com/qje/article-abstract/135/4/2135/5860784> | [china-firm-pollution](../datasets/china-firm-pollution.md) | 403 | **出版方拒绝自动访问**：同一 Oxford 主机的扫描为 403；本轮没有逐篇绕过验证读取正文，不能确认各页内容。 保留论文证据地址，不完成挑战、不改用未核实的镜像，也不据此降低其关联数据资产的成熟度。 |
| 38 | <https://academic.oup.com/qje/article/139/3/1941/7632762> | [rfd](../datasets/rfd.md) | 403 | **出版方拒绝自动访问**：同一 Oxford 主机的扫描为 403；本轮没有逐篇绕过验证读取正文，不能确认各页内容。 保留论文证据地址，不完成挑战、不改用未核实的镜像，也不据此降低其关联数据资产的成熟度。 |
| 39 | <https://academic.oup.com/restud/advance-article/doi/10.1093/restud/rdag047/8688845> | [asif](../datasets/asif.md), [china-second-industrial-survey-1985](../datasets/china-second-industrial-survey-1985.md), [china-steel-plant-performance-reports](../datasets/china-steel-plant-performance-reports.md) | 403 | **出版方拒绝自动访问**：同一 Oxford 主机的扫描为 403；本轮没有逐篇绕过验证读取正文，不能确认各页内容。 保留论文证据地址，不完成挑战、不改用未核实的镜像，也不据此降低其关联数据资产的成熟度。 |
| 40 | <https://academic.oup.com/restud/advance-article/doi/10.1093/restud/rdag078/8737903> | [asif](../datasets/asif.md), [china-census](../datasets/china-census.md), [china-million-rouble-plant-register](../datasets/china-million-rouble-plant-register.md), [china-patents](../datasets/china-patents.md) | 403 | **出版方拒绝自动访问**：同一 Oxford 主机的扫描为 403；本轮没有逐篇绕过验证读取正文，不能确认各页内容。 保留论文证据地址，不完成挑战、不改用未核实的镜像，也不据此降低其关联数据资产的成熟度。 |
| 41 | <https://academic.oup.com/restud/article/92/6/3611/8099437> | [asif](../datasets/asif.md) | 403 | **出版方拒绝自动访问**：同一 Oxford 主机的扫描为 403；本轮没有逐篇绕过验证读取正文，不能确认各页内容。 保留论文证据地址，不完成挑战、不改用未核实的镜像，也不据此降低其关联数据资产的成熟度。 |
| 42 | <https://api.figshare.com/v2/articles/9828827> | [china-harmonized-nighttime-lights-li-et-al](../datasets/china-harmonized-nighttime-lights-li-et-al.md), [china-nighttime-lights](../datasets/china-nighttime-lights.md) | 400 | **请求方式差异**：GitHub HEAD 返回 400；普通浏览器 GET 原 API URL 返回对应夜间灯光数据的 JSON 文件清单和下载链接。 保留 API URL；这是 HEAD 检查误报，尚未更改检查器的重试策略，也没有验证所有 TIFF 下载。 |
| 43 | <https://api.github.com/search/repositories> | [china-trademarks](../datasets/china-trademarks.md) | 422 | **API 需参数**：GET 原 URL 返回 422，明确 q 参数缺失；记录把它当作检索 API 起点，不是数据下载文件。 保留 API 语义；使用时传入实际查询，不加随意查询来让检查变绿。 |
| 44 | <https://api.semanticscholar.org/graph/v1/paper/DOI:10.3368/jhr.0122-12126r2> | [china-employer-employee-matched-admin](../datasets/china-employer-employee-matched-admin.md) | 429 | **API 限流**：GitHub 返回 429；读取器未取得响应内容。 保留为文献元数据线索，稍后按服务规则重试；不把它等同于原数据不可得。 |
| 45 | <https://bbs.baobeihuijia.com/> | [china-trafficked-children-inflow](../datasets/china-trafficked-children-inflow.md) | 521 | **服务异常**：论坛 GitHub 返回 521，读取器未取得内容；同项目主页也为 521。 保留并待源站恢复；没有可验证的新论坛地址。 |
| 46 | <https://bmfw.www.gov.cn/yqfxdjcx/risk.html> | [china-county-daily-covid-risk-level-2020-2022](../datasets/china-county-daily-covid-risk-level-2020-2022.md) | URLError | **已知历史退役**：扫描 DNS 失败；疫情风险等级记录本已说明国家工具于 2022-12-16 下线。 不修造一个现行疫情风险接口；历史公布源和作者后续发布的表格分开。 |
| 47 | <https://broomcenter.ucsb.edu/sites/default/files/publications/pdf/kuhn3.pdf> | [china-census](../datasets/china-census.md), [china-zhaopin-job-ads-2008-2010](../datasets/china-zhaopin-job-ads-2008-2010.md) | 404 | **旧 PDF 404**：GitHub 和浏览器均确认 UCSB 的旧 kuhn3.pdf 返回 404。 招聘广告记录已把此文档路线标为待复核；保留过往阅读证据和独立作者复现页，不用不同版本工作论文悄悄替换。 |
| 48 | <https://caser.shanghai.nyu.edu/caser-projects/hkpssd/> | [china-hkpssd-geocoded-survey-2026](../datasets/china-hkpssd-geocoded-survey-2026.md) | URLError | **TLS 未确认**：GitHub 证书链验证失败；读取器超时。 保留 NYU Shanghai 项目页；未关闭证书验证或绕过浏览器警告。 |
| 49 | <https://cbdb.hsites.harvard.edu/sites/g/files/omnuum3101/files/cbdb/files/hedging_desperation_how_kinship_networks_reduced_cannibalism_in_historical_china.pdf> | [china-historical-clan-kinship-1470-1910](../datasets/china-historical-clan-kinship-1470-1910.md) | 403 | **索引内容可读**：扫描 HEAD 403；网页读取器可提取原 URL 的 22 页论文（标注上周抓取）。 至少不是已证明的失效来源；缓存正文不保证此刻每个网络都可直接 GET，保留原文证据。 |
| 50 | <https://cdn.sciengine.com/doi/pdf/78B62CC0207F48519A8AB26B1BD41018> | [china-mofcom-rural-ecommerce-demo-counties](../datasets/china-mofcom-rural-ecommerce-demo-counties.md) | URLError | **未确认**：GitHub DNS 失败；尚未取得独立 PDF 内容。 保留 Science China DOI/PDF 来源；下一步核对出版方 DOI 页面和文件身份，不拿摘要补全文细节。 |
| 51 | <https://cem.cau.edu.cn/art/2026/4/17/art_36277_1108087.html> | [cfps](../datasets/cfps.md) | URLError | **未确认**：GitHub 连接重置；读取器超时。 是 CFPS 的机构介绍证据，不是 CFPS 原始数据申请入口，保留待复核。 |
| 52 | <https://ceps.ruc.edu.cn/xmjs/xmgk.htm> | [ceps](../datasets/ceps.md) | URLError | **TLS 未确认**：GitHub 报自签名证书；读取器超时。 不绕过证书检查。RUC 新平台正式公告已列 CEPS 数据空间，可作为后续核对线索，但本轮未核实其具体文件权限，不替换全部 CEPS 说明。 |
| 53 | <https://cesi.econ.cuhk.edu.hk/wp-content/uploads/PPT_Keyang_Li.pdf> | [china-employer-employee-matched-admin](../datasets/china-employer-employee-matched-admin.md) | 403 | **索引内容可读**：扫描 HEAD 403；读取器可提取原 URL 的 51 页 CESI 报告（标注两天前抓取）。 保留论文报告来源。报告能读不证明雇主—雇员行政微观数据可下载。 |
| 54 | <https://chfs.swufe.edu.cn/sjzx.htm> | [chfs](../datasets/chfs.md) | 404 | **404／官方新路线**：GitHub 与浏览器均确认旧页 404；官网当前申请说明正式链接 https://chfser.swufe.edu.cn/data/，可到登录页。 CHFS 已更新；六轮 2011-2021 可申请，2023/2025 调查完成不等于一般公开申请，未登录或提交申请。 |
| 55 | <https://colab.ws/articles/10.1016%2Fj.jfineco.2021.05.028> | [wind](../datasets/wind.md) | 403 | **受工具限制**：扫描 403；浏览器复核被导航策略阻止。 这是 Wind 的第三方论文元数据来源；不以此否定 Wind 模块或订阅，不绕过限制。 |
| 56 | <https://css.sysu.edu.cn/Data> | [clds](../datasets/clds.md) | URLError | **未确认**：GitHub 超时；读取器亦未取得页面。 保留 CLDS 官方数据页，待机构正常网络确认申请情况；不推断停更或数据消失。 |

## 后续复核的止点

没有正式新址或独立内容证据的条目仍未确认：尤其是法院平台、SRES、若干地方通知、水质端口、HKPSSD/CEPS 的 TLS 与 CLDS 页面。它们需要服务恢复或合法机构网络/人工访问，而不是继续猜域名。Oxford 11 项是出版方访问限制，其中一项实见验证页，其余不冒充逐篇读过。Figshare 原 GET 能返回文件清单而 HEAD 400，GitHub 搜索 API 缺 q 时 422，以及 Semantic Scholar 429，均不应触发删除数据记录。旧疫情工具已在记录中说明退役，不应伪造一个现在仍在服务的历史工具。

新的取数路径仅按官方公告和目录更新；旧 URL 为保存证据仍留在正文或 provenance，因此后续扫描仍可能报告它们。这不代表修复没生效。下轮应依据本表优先复查会改变数据获取决策的服务，而不是把所有历史引用“刷绿”。
