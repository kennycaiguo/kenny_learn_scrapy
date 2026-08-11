在 Scrapy 中，自定义管道（Pipeline）**唯一必须实现的方法只有 1 个**：`process_item(self, item, spider)`。 

除此之外，还有几个常用的**可选**方法，常用于爬虫开启、关闭或初始化配置。

必须实现的方法

- `process_item(self, item, spider)`
  - **作用**：核心方法，负责处理每个被爬虫提取出来的 Item 对象。
  - **返回值**：必须返回一个 Item 对象（或抛出 `DropItem` 异常），返回的 Item 会被传给后续的 Pipeline 继续处理。

常见可选方法

- `open_spider(self, spider)`
  - **作用**：当爬虫刚启动、被打开时自动调用一次。
  - **常用场景**：在这里建立数据库连接、打开文件或初始化外部资源。
- `close_spider(self, spider)`
  - **作用**：当爬虫关闭、结束时自动调用一次。
  - **常用场景**：在这里关闭数据库连接、安全保存并关闭文件。
- `from_crawler(cls, crawler)`
  - **作用**：通过类方法获取 Scrapy 的核心组件和配置。
  - **常用场景**：用于从 `settings.py` 读取自定义配置参数。