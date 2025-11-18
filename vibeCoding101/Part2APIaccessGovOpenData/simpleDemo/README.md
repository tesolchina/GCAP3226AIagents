<<<<<<< HEAD
# How to Retrieve "Population by Sex and Age Group" Dataset via API

## Dataset Overview
This dataset provides population statistics for Hong Kong, broken down by sex and age group. It is available in English, Traditional Chinese, and Simplified Chinese.

## API Endpoints
You can retrieve the data in JSON format using the following API endpoints:

- **English:**
  https://www.censtatd.gov.hk/api/get.php?id=110-01001&lang=en&full_series=1
- **Traditional Chinese:**
  https://www.censtatd.gov.hk/api/get.php?id=110-01001&lang=tc&full_series=1
- **Simplified Chinese:**
  https://www.censtatd.gov.hk/api/get.php?id=110-01001&lang=sc&full_series=1

## How to Use the API
You do not need an API key. Just copy and paste the link into your browser or use a tool like Excel, Python, or R to fetch the data.

### Example (for non-programmers)

#### Using a Web Browser
1. Copy the English API link above.
2. Paste it into your browser's address bar and press Enter.
3. The browser will show the data in JSON format.

#### Using Excel
1. Open Excel.
2. Go to the "Data" tab.
3. Click "From Web".
4. Paste the API link and click OK.
5. Excel will import the data.

#### Using Python (pseudocode)
```
# Pseudocode for fetching data
set url to "https://www.censtatd.gov.hk/api/get.php?id=110-01001&lang=en&full_series=1"
get data from url
show data
```

#### Using R (pseudocode)
```
# Pseudocode for fetching data
url <- "https://www.censtatd.gov.hk/api/get.php?id=110-01001&lang=en&full_series=1"
data <- fetch data from url
print data
```

## Data Structure
Each record contains:
- SEX: Male (M), Female (F), or Total
- AGE: Age group (e.g., "0-4", "5-9", ..., "85+", or "Total")
- figure: Percentage of total population
- period: Data period (e.g., "202506" for June 2025)

## More Information
- Maintainer: Demographic Statistics Section (1), Census and Statistics Department
- Email: population@censtatd.gov.hk
- Phone: (852) 3903 6943

For more details, visit the [dataset page](https://data.gov.hk/en-data/dataset/hk-censtatd-tablechart-110-01001).
=======
# 香港天文台每日总降雨量数据集 API 获取说明

## 数据集简介
- 数据来源：[香港政府一站通开放数据平台 - 每日总降雨量](https://data.gov.hk/sc-data/dataset/hk-hko-rss-daily-total-rainfall)
- 数据内容：香港各区每日总降雨量，按天更新。

## 可用数据与API说明
1. 该数据集通过 RSS（XML）格式提供，适合自动化抓取。
2. RSS 数据地址（示例）：
   - [https://data.gov.hk/filestore/feeds/data_rss_sc.xml](https://data.gov.hk/filestore/feeds/data_rss_sc.xml)
   - 你可以在页面底部“RSS摘要”部分找到实际的 RSS 链接。
3. 通过 RSS 订阅工具或编程方式（如 Python、Javascript）可定期获取最新数据。

## 获取数据的伪代码（适合非程序员理解）

1. 打开数据集页面，找到“RSS摘要”或“RSS Feed”部分，复制 RSS 链接。
2. 用下列伪代码获取数据：

```
步骤1：复制RSS数据链接（如：https://data.gov.hk/filestore/feeds/data_rss_sc.xml）
步骤2：在浏览器或RSS阅读器中粘贴并访问该链接，可直接查看XML格式数据
步骤3：如需自动化处理，可用如下伪代码：

伪代码：
- 设定数据链接 = 'https://data.gov.hk/filestore/feeds/data_rss_sc.xml'
- 用工具（如Excel、Python脚本、在线RSS解析器）打开该链接
- 解析XML内容，查找每日降雨量相关条目
- 提取你需要的日期、地区、降雨量等信息
- 保存或分析数据
```

## 进阶说明
- 若需批量下载历史数据，可在数据集页面选择日期范围后，按页面指引下载。
- 如需API技术细节，可参考页面底部“API规格”链接。

## 联系方式
- 数据维护：香港天文台
- 查询邮箱：mailbox@hko.gov.hk

---
如需进一步自动化脚本或详细操作指南，请联系数据管理员或参考香港政府开放数据平台帮助文档。
# 香港天文台每日总降雨量数据集 API 获取说明

## 数据集简介
- 数据来源：[香港政府一站通开放数据平台 - 每日总降雨量](https://data.gov.hk/sc-data/dataset/hk-hko-rss-daily-total-rainfall)
- 数据内容：香港各区每日总降雨量，按天更新。

## 可用数据与API说明
1. 该数据集通过 RSS（XML）格式提供，适合自动化抓取。
2. RSS 数据地址（示例）：
   - [https://data.gov.hk/filestore/feeds/data_rss_sc.xml](https://data.gov.hk/filestore/feeds/data_rss_sc.xml)
   - 你可以在页面底部“RSS摘要”部分找到实际的 RSS 链接。
3. 通过 RSS 订阅工具或编程方式（如 Python、Javascript）可定期获取最新数据。

## 获取数据的伪代码（适合非程序员理解）

1. 打开数据集页面，找到“RSS摘要”或“RSS Feed”部分，复制 RSS 链接。
2. 用下列伪代码获取数据：

```
步骤1：复制RSS数据链接（如：https://data.gov.hk/filestore/feeds/data_rss_sc.xml）
步骤2：在浏览器或RSS阅读器中粘贴并访问该链接，可直接查看XML格式数据
步骤3：如需自动化处理，可用如下伪代码：

伪代码：
- 设定数据链接 = 'https://data.gov.hk/filestore/feeds/data_rss_sc.xml'
- 用工具（如Excel、Python脚本、在线RSS解析器）打开该链接
- 解析XML内容，查找每日降雨量相关条目
- 提取你需要的日期、地区、降雨量等信息
- 保存或分析数据
```

## 进阶说明
- 若需批量下载历史数据，可在数据集页面选择日期范围后，按页面指引下载。
- 如需API技术细节，可参考页面底部“API规格”链接。

## 联系方式
- 数据维护：香港天文台
- 查询邮箱：mailbox@hko.gov.hk

---
如需进一步自动化脚本或详细操作指南，请联系数据管理员或参考香港政府开放数据平台帮助文档。
>>>>>>> 719df1b (Save all local changes before rebase)
