Scrapy 可以获取 `alt` 属性却拿不到 `src` 属性，通常是因为网页使用了**图片懒加载（Lazy Load）**。这意味着网页初始源码里的 `src` 只是一个占位图，而真实的图片地址藏在诸如 `data-src`、`data-original` 等自定义属性中，只有当浏览器滚动到该位置时才通过 JavaScript 加载到 `src` 中。 

核心排查与解决办法

- **检查原始 HTML 源码**：
  在浏览器中右键选择“查看网页源代码”（非检查/F12的Elements），或者在 Scrapy 终端中输入 `print(response.text)`。看看 `img` 标签里原本是不是没有 `src`，或者 `src` 的值是一个空白/加载中小图标。
- **修改选择器提取其他属性**：
  如果真实地址在 `data-src` 或 `data-original` 中，请更换提取的目标属性。
  - **XPath 写法**：`//img/@data-src` 或 `//img/@data-original`
  - **CSS 写法**：`img::attr(data-src)` 
- **动态加载（JS 渲染）问题**：
  如果 `src` 是纯粹由前端 JS 动态完整拼装且不在 HTML 源码的任何自定义属性中，Scrapy 静态爬虫无法直接获取，需要结合 **[⁠Selenium](https://selenium-python.readthedocs.io/)** 或 Playwright 等自动化工具进行页面渲染。