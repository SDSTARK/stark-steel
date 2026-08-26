/* =========================================================
   Stark Steel - Language Switcher (EN / 中文)
========================================================= */
(function () {
  // Translation dictionary
  const dict = {
    en: {
      // Top bar / header nav
      navHome: "Home",
      navAbout: "About Us",
      navProducts: "Products",
      navNews: "News",
      navContact: "Contact Us",
      navQuote: "Get a Quote",
      topEmail: "esmestarksteel@163.com",
      topPhone: "+86 18954492649",
      topWhatsApp: "WhatsApp",
      topLang: "Language",

      // Hero
      heroSub1: "Worry-free After-sales Service",
      heroTitle1: "Strict order review at Stark-Steel guarantees customer satisfaction.",
      heroSub2: "Professional Team",
      heroTitle2: "Professional pre-sales and after-sales team in the steel industry.",
      btnLearnMore: "Learn More →",
      btnContact: "Contact Us",
      btnReadMore: "Read More →",

      // Section titles
      secProducts: "Products Catalog",
      secProductsSub: "High quality steel products for global customers",
      secRelated: "Related Products",
      secRelatedSub: "Other products you may be interested in",
      secInquiry: "Send Us Your Inquiry",
      secInquirySub: "For more information or to place an order, please contact our sales team. We reply within 24 hours.",

      // Category tabs
      catAll: "All",
      catCarbon: "Carbon Steel",
      catGalvanized: "Galvanized Steel",
      catStainless: "Stainless Steel",
      catAluminum: "Aluminum",
      catRebar: "Steel Rebars",
      catCorrugated: "Corrugated Board",
      catStructural: "Structural Steel",
      catScaffolding: "Scaffolding",
      catNails: "Nails",

      // Product detail
      pdDescription: "Description",
      pdKeyFeatures: "Key Features",
      pdApplications: "Applications",
      pdSizes: "Available Sizes & Specifications",
      pdQuality: "Quality & Packaging",
      pdChatWhatsApp: "Chat on WhatsApp",
      pdGetQuote: "Get a Quote",

      // Form labels
      formName: "Your Name *",
      formNamePh: "Your full name",
      formEmail: "Email Address *",
      formEmailPh: "Your email address",
      formPhone: "Phone / WhatsApp",
      formPhonePh: "+86 0000000000",
      formProduct: "Product of Interest",
      formSubject: "Subject",
      formSubjectPh: "e.g. Inquiry for Steel Products",
      formMessage: "Your Message *",
      formMessagePh: "Tell us the specifications, quantity and destination port...",
      formSend: "Send Message",
      formPrivacy: "* We respect your privacy. Your information will only be used to reply to your inquiry.",
      formSuccess: "Thank you! Your inquiry has been received. We will reply within 24 hours.",

      // Footer
      footerAbout: "Shandong Stark Steel",
      footerAboutText: "We provide high-quality Carbon Steel, Galvanized Steel, Stainless Steel, Aluminum and Corrugated Board with reliable service to global customers.",
      footerLinks: "Quick Links",
      footerCategories: "Product Categories",
      footerContact: "Contact",
      footerCopyright: "All rights reserved.",

      // Index page extras
      aboutProductsOverline: "About Products",
      aboutProductsTitle: "Professional Steel Supplier You Can Trust",
      aboutProductsText: "Shandong Stark Steel Co., Ltd is a professional supplier focusing on Carbon Steel, Galvanized Steel, Stainless Steel, Aluminum and Corrugated Board. We provide high-quality products, complete specifications and reliable after-sales service, serving global customers with integrity and professionalism.",
      statClients: "Satisfied Clients",
      statReviews: "Five-Star Reviews",
      statProjects: "Completed Projects",
      statLines: "Production Lines",
      inquiryPriceTitle: "Get the Latest Price",
      inquiryPriceSub: "Feel Free To Contact Us",
      contactInfoTitle: "Contact Information",
      directContactTitle: "Get In Touch Directly",
      contactPerson: "Contact",

      // Breadcrumb
      bcHome: "Home",
      bcProducts: "Products",

      // Common labels
      category: "Category:",
      hotBadge: "Hot",
      specs: "Specifications",
      contactSales: "Contact Sales",

      // About page
      aboutTitle: "About Shandong Stark Steel",
      aboutSub: "Reliable steel supplier with professional service",

      // News page
      newsTitle: "News & Updates",
      newsSub: "Latest information from Shandong Stark Steel",

      // Contact page
      contactTitle: "Contact Us",
      contactSub: "Get in touch with our sales team",
      contactPhone: "Phone",
      contactEmail: "Email",
      contactAddress: "Address",
      contactWhatsApp: "WhatsApp",

      // Product 15 (Nails)
      p15Title: "Steel Wire Nails",
      p15Cat: "Carbon Steel / Nails",
      p15Summary: "High quality steel wire nails manufactured from Q195/Q235 low carbon steel wire. Available in bright, galvanized and painted finishes for construction, carpentry, packaging and general fastening applications. Smooth shank, diamond point and flat head ensure easy driving and secure holding.",
      p15DescP1: "Steel wire nails are one of the most widely used fasteners in construction, woodworking and packaging industries. Our nails are produced from high quality low carbon steel wire (Q195 / Q235) with uniform shank diameter, consistent hardness and sharp diamond points for smooth penetration into wood, concrete formwork and other materials.",
      p15DescP2: "We supply common wire nails, roofing nails, concrete nails, finishing nails and U-type nails in a wide range of diameters and lengths. Surface options include bright polished, electro-galvanized, hot-dip galvanized and color painted to suit indoor, outdoor and corrosion-resistant requirements.",
      p15DescP3: "Each batch is inspected for dimensions, tensile strength and surface finish. Nails are packed in bulk cartons, small boxes, plastic bags or on pallets for export shipment, ensuring they arrive at site ready for immediate use.",
      p15Feature1: "Selected low carbon steel wire with good ductility and consistent mechanical properties.",
      p15Feature2: "Smooth shank, sharp diamond point and flat head for easy driving and firm holding.",
      p15Feature3: "Bright, electro-galvanized, hot-dip galvanized and painted finishes available.",
      p15Feature4: "Full range of sizes from 1.0 mm to 5.0 mm diameter and 20 mm to 120 mm length.",
      p15Feature5: "Clean surface, no oil stains, uniform coating thickness for galvanized types.",
      p15Feature6: "Custom packaging, private labeling and mixed container loading supported.",
      p15App: "Steel wire nails are widely used in building construction, wooden formwork, furniture manufacturing, pallet and crate assembly, roofing felt fixing, drywall installation, interior decoration, packaging and general DIY projects. They are suitable for hand nailing, pneumatic nail guns and automated fastening equipment.",
      p15Quality: "Nails are checked for length, diameter, point angle and bending strength before packing. Galvanized nails meet zinc coating requirements for indoor and outdoor use. Packaging options include 25kg cartons, 1kg/5kg small boxes, plastic buckets and palletized bulk bags. All shipments are packed in seaworthy containers for safe export transport."
    },
    zh: {
      // Top bar / header nav
      navHome: "首页",
      navAbout: "关于我们",
      navProducts: "产品中心",
      navNews: "新闻资讯",
      navContact: "联系我们",
      navQuote: "获取报价",
      topEmail: "esmestarksteel@163.com",
      topPhone: "+86 18954492649",
      topWhatsApp: "WhatsApp",
      topLang: "语言",

      // Hero
      heroSub1: "无忧售后服务",
      heroTitle1: "斯塔克钢铁严格审核每一单，确保客户满意。",
      heroSub2: "专业团队",
      heroTitle2: "钢铁行业专业的售前与售后服务团队。",
      btnLearnMore: "了解更多 →",
      btnContact: "联系我们",
      btnReadMore: "查看详情 →",

      // Section titles
      secProducts: "产品目录",
      secProductsSub: "为全球客户提供高品质钢铁产品",
      secRelated: "相关产品",
      secRelatedSub: "您可能感兴趣的其他产品",
      secInquiry: "发送询盘",
      secInquirySub: "如需了解更多信息或下单，请联系我们的销售团队，我们将在24小时内回复。",

      // Category tabs
      catAll: "全部",
      catCarbon: "碳钢",
      catGalvanized: "镀锌钢",
      catStainless: "不锈钢",
      catAluminum: "铝材",
      catRebar: "钢筋",
      catCorrugated: "彩钢板",
      catStructural: "结构钢",
      catScaffolding: "脚手架",
      catNails: "钉子",

      // Product detail
      pdDescription: "产品描述",
      pdKeyFeatures: "主要特点",
      pdApplications: "应用领域",
      pdSizes: "规格尺寸",
      pdQuality: "质量与包装",
      pdChatWhatsApp: "WhatsApp 咨询",
      pdGetQuote: "获取报价",

      // Form labels
      formName: "您的姓名 *",
      formNamePh: "请输入您的姓名",
      formEmail: "电子邮箱 *",
      formEmailPh: "请输入您的邮箱地址",
      formPhone: "电话 / WhatsApp",
      formPhonePh: "+86 0000000000",
      formProduct: "感兴趣的产品",
      formSubject: "主题",
      formSubjectPh: "例如：钢材产品询盘",
      formMessage: "您的留言 *",
      formMessagePh: "请告知规格、数量和目的港...",
      formSend: "发送留言",
      formPrivacy: "* 我们尊重您的隐私，您的信息仅用于回复您的询盘。",
      formSuccess: "谢谢！您的询盘已收到，我们将在24小时内回复。",

      // Footer
      footerAbout: "山东斯塔克钢铁",
      footerAboutText: "我们为全球客户提供高品质的碳钢、镀锌钢、不锈钢、铝材和彩钢板产品及可靠服务。",
      footerLinks: "快速链接",
      footerCategories: "产品分类",
      footerContact: "联系方式",
      footerCopyright: "版权所有。",

      // 首页补充
      aboutProductsOverline: "关于产品",
      aboutProductsTitle: "值得信赖的专业钢材供应商",
      aboutProductsText: "山东斯塔克钢铁有限公司是一家专注于碳钢、镀锌钢、不锈钢、铝材和彩钢板的专业供应商。我们提供高品质产品、齐全规格和可靠的售后服务，以诚信和专业服务全球客户。",
      statClients: "满意客户",
      statReviews: "五星好评",
      statProjects: "完成项目",
      statLines: "生产线",
      inquiryPriceTitle: "获取最新价格",
      inquiryPriceSub: "欢迎随时联系我们",
      contactInfoTitle: "联系信息",
      directContactTitle: "直接取得联系",
      contactPerson: "联系人",

      // Breadcrumb
      bcHome: "首页",
      bcProducts: "产品中心",

      // Common labels
      category: "分类：",
      hotBadge: "热销",
      specs: "规格参数",
      contactSales: "联系销售",

      // About page
      aboutTitle: "关于山东斯塔克钢铁",
      aboutSub: "值得信赖的钢材供应商，提供专业服务",

      // News page
      newsTitle: "新闻与动态",
      newsSub: "山东斯塔克钢铁的最新资讯",

      // Contact page
      contactTitle: "联系我们",
      contactSub: "与我们的销售团队取得联系",
      contactPhone: "电话",
      contactEmail: "邮箱",
      contactAddress: "地址",
      contactWhatsApp: "WhatsApp",

      // Product 15 (Nails)
      p15Title: "钢钉",
      p15Cat: "碳钢 / 钉子",
      p15Summary: "采用Q195/Q235低碳钢丝制造的高品质钢钉。提供光面、镀锌和喷漆等多种表面处理，适用于建筑、木工、包装及一般紧固应用。光圆钉杆、菱形钉尖和扁平钉头确保易于敲击和牢固固定。",
      p15DescP1: "钢钉是建筑、木工和包装行业中最常用的紧固件之一。我们的钢钉采用优质低碳钢丝（Q195/Q235）生产，钉杆直径均匀、硬度一致、钉尖锋利呈菱形，可顺畅钉入木材、建筑模板及其他材料。",
      p15DescP2: "我们供应普通圆钉、瓦楞钉、水泥钉、 finish 钉和U型钉等多种类型，直径和长度范围齐全。表面处理可选择光面抛光、电镀锌、热浸镀锌和彩色喷漆，以满足室内、室外及耐腐蚀等不同使用环境的要求。",
      p15DescP3: "每批钢钉在出厂前均经过尺寸、抗拉强度和表面质量检验。产品采用散装纸箱、小盒、塑料袋或托盘包装，便于出口运输，确保到达现场即可投入使用。",
      p15Feature1: "精选低碳钢丝，具有良好的延展性和稳定的机械性能。",
      p15Feature2: "光圆钉杆、锋利菱形钉尖和扁平钉头，易于敲击且夹持牢固。",
      p15Feature3: "可选光面、电镀锌、热浸镀锌和喷漆等多种表面处理。",
      p15Feature4: "规格齐全，直径1.0-5.0mm，长度20-120mm可定制。",
      p15Feature5: "表面洁净无油污，镀锌层厚度均匀。",
      p15Feature6: "支持定制包装、贴牌以及混装集装箱出货。",
      p15App: "钢钉广泛应用于建筑施工、木模板制作、家具制造、托盘和木箱组装、屋面毡固定、石膏板安装、室内装饰、包装以及各类DIY项目，适用于手工锤击、气动钉枪和自动化紧固设备。",
      p15Quality: "钢钉在包装前均经过长度、直径、钉尖角度和抗弯强度检查。镀锌钉满足室内外使用的锌层要求。包装方式包括25公斤纸箱、1公斤/5公斤小盒、塑料桶和托盘集装袋，所有货物均采用适合海运的集装箱包装，确保出口运输安全。"
    }
  };

  const getText = (key, lang) => {
    if (dict[lang] && dict[lang][key]) return dict[lang][key];
    if (dict.en[key]) return dict.en[key];
    return null;
  };

  const applyLang = (lang) => {
    document.documentElement.lang = lang === 'zh' ? 'zh-CN' : 'en';
    localStorage.setItem('stark-steel-lang', lang);

    document.querySelectorAll('[data-i18n]').forEach(el => {
      const key = el.dataset.i18n;
      const text = getText(key, lang);
      if (text !== null) {
        // For elements that should keep child links, only replace text nodes if complex
        if (el.children.length === 0) {
          el.textContent = text;
        } else {
          // Update direct text before first child if any
          const firstText = Array.from(el.childNodes).find(n => n.nodeType === 3 && n.textContent.trim());
          if (firstText) firstText.textContent = text + ' ';
          else if (!el.querySelector('[data-i18n]')) el.textContent = text;
        }
      }
    });

    // Update placeholders
    document.querySelectorAll('[data-i18n-placeholder]').forEach(el => {
      const key = el.dataset.i18nPlaceholder;
      const text = getText(key, lang);
      if (text !== null) el.placeholder = text;
    });

    // Update active state on switcher buttons
    document.querySelectorAll('.lang-switch-btn').forEach(btn => {
      btn.classList.toggle('active', btn.dataset.lang === lang);
    });

    // Dispatch event for other scripts
    window.dispatchEvent(new CustomEvent('starkLanguageChanged', { detail: { lang } }));
  };

  const renderSwitcher = () => {
    document.querySelectorAll('.lang-switch').forEach(container => {
      // Avoid double render
      if (container.querySelector('.lang-switch-btn')) return;
      container.innerHTML =
        '<button class="lang-switch-btn" data-lang="en" type="button">EN</button>' +
        '<span style="opacity:.6;margin:0 2px;">/</span>' +
        '<button class="lang-switch-btn" data-lang="zh" type="button">中</button>';
    });

    document.querySelectorAll('.lang-switch-btn').forEach(btn => {
      btn.addEventListener('click', () => applyLang(btn.dataset.lang));
    });
  };

  const init = () => {
    renderSwitcher();
    const saved = localStorage.getItem('stark-steel-lang') || 'en';
    applyLang(saved);
  };

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

  // Expose API
  window.StarkI18n = { applyLang, getText };
})();
