# -*- coding: utf-8 -*-
import json, re, os

ROOT = os.path.dirname(os.path.abspath(__file__))

# entries: (file, key, old_html, new_html, en_text)
# For elements with <br> or <strong>, we flatten to a single text node so applyLang translates fully.
E = []

# ---------------- about.html ----------------
A = 'about.html'
E += [
 (A, 'aboutBannerTitle', '<h1>About Us</h1>', '<h1 data-i18n="aboutBannerTitle">About Us</h1>', 'About Us'),
 (A, 'aboutOverline', '<span class="overline">About Shandong Stark Steel Co., Ltd</span>', '<span class="overline" data-i18n="aboutOverline">About Shandong Stark Steel Co., Ltd</span>', 'About Shandong Stark Steel Co., Ltd'),
 (A, 'aboutLead1', '<h2>We have cooperated with this steel company for many years.</h2>', '<h2 data-i18n="aboutLead1">We have cooperated with this steel company for many years.</h2>', 'We have cooperated with this steel company for many years.'),
 (A, 'aboutLead2', '<p>Stable product quality, reasonable price and thoughtful after-sales service.</p>', '<p data-i18n="aboutLead2">Stable product quality, reasonable price and thoughtful after-sales service.</p>', 'Stable product quality, reasonable price and thoughtful after-sales service.'),
 (A, 'aboutWhoTitle', '<h3>Who We Are</h3>', '<h3 data-i18n="aboutWhoTitle">Who We Are</h3>', 'Who We Are'),
 (A, 'aboutWho1', '<p>Shandong Stark Steel Co., Ltd is a reliable metal materials enterprise based in Liaocheng, China\'s major steel industrial hub, with its office at Xingguang International Financial Center. Benefiting from convenient transport and complete supporting facilities, we realize efficient operation, punctual delivery and global business expansion.</p>', '<p data-i18n="aboutWho1">Shandong Stark Steel Co., Ltd is a reliable metal materials enterprise based in Liaocheng, China\'s major steel industrial hub, with its office at Xingguang International Financial Center. Benefiting from convenient transport and complete supporting facilities, we realize efficient operation, punctual delivery and global business expansion.</p>', 'Shandong Stark Steel Co., Ltd is a reliable metal materials enterprise based in Liaocheng, China\'s major steel industrial hub, with its office at Xingguang International Financial Center. Benefiting from convenient transport and complete supporting facilities, we realize efficient operation, punctual delivery and global business expansion.'),
 (A, 'aboutWho2', '<p>We integrate R&D, production, sales and after-sales service of four core products: <strong>carbon steel, galvanized steel, stainless steel and aluminum</strong>. Our full-range carbon steel covers low, medium and high carbon grades with outstanding mechanical performance and cost advantages, widely used in pipelines, construction, machinery, auto frames and steel structure engineering.</p>', '<p data-i18n="aboutWho2">We integrate R&D, production, sales and after-sales service of four core products: carbon steel, galvanized steel, stainless steel and aluminum. Our full-range carbon steel covers low, medium and high carbon grades with outstanding mechanical performance and cost advantages, widely used in pipelines, construction, machinery, auto frames and steel structure engineering.</p>', 'We integrate R&D, production, sales and after-sales service of four core products: carbon steel, galvanized steel, stainless steel and aluminum. Our full-range carbon steel covers low, medium and high carbon grades with outstanding mechanical performance and cost advantages, widely used in pipelines, construction, machinery, auto frames and steel structure engineering.'),
 (A, 'aboutTenet', '<div class="tenet-quote">Quality First · Customer-Oriented · Integrity-Based · Win-Win Development</div>', '<div class="tenet-quote" data-i18n="aboutTenet">Quality First · Customer-Oriented · Integrity-Based · Win-Win Development</div>', 'Quality First · Customer-Oriented · Integrity-Based · Win-Win Development'),
 (A, 'aboutTenetDesc', '<p>Sticking to the tenet of "Quality First, Customer-Oriented, Integrity-Based, Win-Win Development", we implement full-process quality inspection to meet international standards. Our experienced team provides customized products and technical consulting.</p>', '<p data-i18n="aboutTenetDesc">Sticking to the tenet of "Quality First, Customer-Oriented, Integrity-Based, Win-Win Development", we implement full-process quality inspection to meet international standards. Our experienced team provides customized products and technical consulting.</p>', 'Sticking to the tenet of "Quality First, Customer-Oriented, Integrity-Based, Win-Win Development", we implement full-process quality inspection to meet international standards. Our experienced team provides customized products and technical consulting.'),
 (A, 'aboutClients', '<p>Relying on local industrial cluster strengths, we maintain long-term stable cooperation with clients from Europe, America, Southeast Asia and the Middle East. We strive to be a top global metal supplier and sincerely welcome worldwide partners for joint development.</p>', '<p data-i18n="aboutClients">Relying on local industrial cluster strengths, we maintain long-term stable cooperation with clients from Europe, America, Southeast Asia and the Middle East. We strive to be a top global metal supplier and sincerely welcome worldwide partners for joint development.</p>', 'Relying on local industrial cluster strengths, we maintain long-term stable cooperation with clients from Europe, America, Southeast Asia and the Middle East. We strive to be a top global metal supplier and sincerely welcome worldwide partners for joint development.'),
 (A, 'aboutWhyTitle', '<h3>Why Choose Us</h3>', '<h3 data-i18n="aboutWhyTitle">Why Choose Us</h3>', 'Why Choose Us'),
 (A, 'aboutWhy1', '<li>More than 20 years of steel trading and manufacturing experience</li>', '<li data-i18n="aboutWhy1">More than 20 years of steel trading and manufacturing experience</li>', 'More than 20 years of steel trading and manufacturing experience'),
 (A, 'aboutWhy2', '<li>Complete specifications for all product categories, supporting customization</li>', '<li data-i18n="aboutWhy2">Complete specifications for all product categories, supporting customization</li>', 'Complete specifications for all product categories, supporting customization'),
 (A, 'aboutWhy3', '<li>Full-process quality inspection to meet international standards (GB / ASTM / JIS / DIN / EN)</li>', '<li data-i18n="aboutWhy3">Full-process quality inspection to meet international standards (GB / ASTM / JIS / DIN / EN)</li>', 'Full-process quality inspection to meet international standards (GB / ASTM / JIS / DIN / EN)'),
 (A, 'aboutWhy4', '<li>Third-party inspection such as SGS, BV, TUV is acceptable</li>', '<li data-i18n="aboutWhy4">Third-party inspection such as SGS, BV, TUV is acceptable</li>', 'Third-party inspection such as SGS, BV, TUV is acceptable'),
 (A, 'aboutWhy5', '<li>Professional and efficient service from inquiry to shipment</li>', '<li data-i18n="aboutWhy5">Professional and efficient service from inquiry to shipment</li>', 'Professional and efficient service from inquiry to shipment'),
 (A, 'aboutWhy6', '<li>Long-term stable cooperation with clients worldwide</li>', '<li data-i18n="aboutWhy6">Long-term stable cooperation with clients worldwide</li>', 'Long-term stable cooperation with clients worldwide'),
 (A, 'aboutAdvOverline', '<span class="overline">Our Advantages</span>', '<span class="overline" data-i18n="aboutAdvOverline">Our Advantages</span>', 'Our Advantages'),
 (A, 'aboutAdvTitle', '<h2>We can do it best!</h2>', '<h2 data-i18n="aboutAdvTitle">We can do it best!</h2>', 'We can do it best!'),
 (A, 'aboutAdv1', '<li>✓ Steel management support — professional service from inquiry to shipment</li>', '<li data-i18n="aboutAdv1">✓ Steel management support — professional service from inquiry to shipment</li>', '✓ Steel management support — professional service from inquiry to shipment'),
 (A, 'aboutAdv2', '<li>✓ Strict quality inspection — quick response to all professional questions</li>', '<li data-i18n="aboutAdv2">✓ Strict quality inspection — quick response to all professional questions</li>', '✓ Strict quality inspection — quick response to all professional questions'),
 (A, 'aboutAdv3', '<li>✓ Customization support — participate in design, one-stop purchasing</li>', '<li data-i18n="aboutAdv3">✓ Customization support — participate in design, one-stop purchasing</li>', '✓ Customization support — participate in design, one-stop purchasing'),
 (A, 'aboutAdv4', '<li>✓ High-tech enterprise designated by Chinese authorities</li>', '<li data-i18n="aboutAdv4">✓ High-tech enterprise designated by Chinese authorities</li>', '✓ High-tech enterprise designated by Chinese authorities'),
 (A, 'aboutAdv5', '<li>✓ Well-known Chinese trademark with reliable reputation</li>', '<li data-i18n="aboutAdv5">✓ Well-known Chinese trademark with reliable reputation</li>', '✓ Well-known Chinese trademark with reliable reputation'),
 (A, 'aboutContactBtn', '<a href="contact.html" class="btn btn-primary">Contact Us</a>', '<a href="contact.html" class="btn btn-primary" data-i18n="navContact">Contact Us</a>', 'Contact Us'),
 (A, 'aboutStatsTitle', '<h2>25 Years of Experience</h2>', '<h2 data-i18n="aboutStatsTitle">25 Years of Experience</h2>', '25 Years of Experience'),
 (A, 'aboutStatsSub', '<p>Numbers That Speak For Our Strength</p>', '<p data-i18n="aboutStatsSub">Numbers That Speak For Our Strength</p>', 'Numbers That Speak For Our Strength'),
 (A, 'aboutStatL1', '<div class="exp-title">Satisfied Clients</div>', '<div class="exp-title" data-i18n="aboutStatL1">Satisfied Clients</div>', 'Satisfied Clients'),
 (A, 'aboutStatD1', '<div class="exp-desc">Trusted by customers worldwide</div>', '<div class="exp-desc" data-i18n="aboutStatD1">Trusted by customers worldwide</div>', 'Trusted by customers worldwide'),
 (A, 'aboutStatL2', '<div class="exp-title">Five-Star Reviews</div>', '<div class="exp-title" data-i18n="aboutStatL2">Five-Star Reviews</div>', 'Five-Star Reviews'),
 (A, 'aboutStatD2', '<div class="exp-desc">Positive feedback from partners</div>', '<div class="exp-desc" data-i18n="aboutStatD2">Positive feedback from partners</div>', 'Positive feedback from partners'),
 (A, 'aboutStatL3', '<div class="exp-title">Completed Projects</div>', '<div class="exp-title" data-i18n="aboutStatL3">Completed Projects</div>', 'Completed Projects'),
 (A, 'aboutStatD3', '<div class="exp-desc">Delivered on time with quality</div>', '<div class="exp-desc" data-i18n="aboutStatD3">Delivered on time with quality</div>', 'Delivered on time with quality'),
 (A, 'aboutStatL4', '<div class="exp-title">Production Lines</div>', '<div class="exp-title" data-i18n="aboutStatL4">Production Lines</div>', 'Production Lines'),
 (A, 'aboutStatD4', '<div class="exp-desc">Full-process manufacturing</div>', '<div class="exp-desc" data-i18n="aboutStatD4">Full-process manufacturing</div>', 'Full-process manufacturing'),
 (A, 'aboutTmTitle', '<h2>Our Testimonials</h2>', '<h2 data-i18n="aboutTmTitle">Our Testimonials</h2>', 'Our Testimonials'),
 (A, 'aboutTmSub', '<p>Clients Reviews</p>', '<p data-i18n="aboutTmSub">Clients Reviews</p>', 'Clients Reviews'),
 (A, 'aboutTmQ1', '<p class="tm-text">"Very reliable steel supplier, highly recommended! Great steel quality with standard specifications, neat packaging and fast delivery."</p>', '<p class="tm-text" data-i18n="aboutTmQ1">"Very reliable steel supplier, highly recommended! Great steel quality with standard specifications, neat packaging and fast delivery."</p>', '"Very reliable steel supplier, highly recommended! Great steel quality with standard specifications, neat packaging and fast delivery."'),
 (A, 'aboutTmQ2', '<p class="tm-text">"Stable product quality, reasonable price and thoughtful after-sales service. Always our first choice for carbon steel and galvanized steel orders. Looking forward to long-term partnership."</p>', '<p class="tm-text" data-i18n="aboutTmQ2">"Stable product quality, reasonable price and thoughtful after-sales service. Always our first choice for carbon steel and galvanized steel orders. Looking forward to long-term partnership."</p>', '"Stable product quality, reasonable price and thoughtful after-sales service. Always our first choice for carbon steel and galvanized steel orders. Looking forward to long-term partnership."'),
 (A, 'aboutTmQ3', '<p class="tm-text">"Excellent cost performance for steel materials. Good quality, competitive price and on-time shipment. Will place more orders in the future."</p>', '<p class="tm-text" data-i18n="aboutTmQ3">"Excellent cost performance for steel materials. Good quality, competitive price and on-time shipment. Will place more orders in the future."</p>', '"Excellent cost performance for steel materials. Good quality, competitive price and on-time shipment. Will place more orders in the future."'),
 (A, 'aboutTmR1', '<div class="tm-role">Procurement Manager</div>', '<div class="tm-role" data-i18n="aboutTmR1">Procurement Manager</div>', 'Procurement Manager'),
 (A, 'aboutTmR2', '<div class="tm-role">Purchasing Director</div>', '<div class="tm-role" data-i18n="aboutTmR2">Purchasing Director</div>', 'Purchasing Director'),
 (A, 'aboutTmR3', '<div class="tm-role">Project Engineer</div>', '<div class="tm-role" data-i18n="aboutTmR3">Project Engineer</div>', 'Project Engineer'),
]

# ---------------- contact.html ----------------
C = 'contact.html'
E += [
 (C, 'navContact', '<span>Contact Us</span>', '<span data-i18n="navContact">Contact Us</span>', 'Contact Us'),
 (C, 'contactSub1', '<h2>Need Any Service For Steels?</h2>', '<h2 data-i18n="contactSub1">Need Any Service For Steels?</h2>', 'Need Any Service For Steels?'),
 (C, 'contactSub2', '<p>Contact us with any questions! We reply within 24 hours.</p>', '<p data-i18n="contactSub2">Contact us with any questions! We reply within 24 hours.</p>', 'Contact us with any questions! We reply within 24 hours.'),
 (C, 'contactLocTitle', '<h4>Our Location</h4>', '<h4 data-i18n="contactLocTitle">Our Location</h4>', 'Our Location'),
 (C, 'contactLocAddr', '<p>Shandong Stark Steel Co., Ltd<br>Economic and Technological Development Zone,<br>Liaocheng, Shandong Province, China</p>', '<p data-i18n="contactLocAddr">Shandong Stark Steel Co., Ltd, Economic and Technological Development Zone, Liaocheng, Shandong Province, China</p>', 'Shandong Stark Steel Co., Ltd, Economic and Technological Development Zone, Liaocheng, Shandong Province, China'),
 (C, 'contactEmailTitle', '<h4>Email Address</h4>', '<h4 data-i18n="contactEmailTitle">Email Address</h4>', 'Email Address'),
 (C, 'contactPhoneTitle', '<h4>Phone & WhatsApp</h4>', '<h4 data-i18n="contactPhoneTitle">Phone & WhatsApp</h4>', 'Phone & WhatsApp'),
 (C, 'contactPersonTitle', '<h3>Contact Person</h3>', '<h3 data-i18n="contactPersonTitle">Contact Person</h3>', 'Contact Person'),
 (C, 'contactRole', '<div class="bc-role">Sales Manager</div>', '<div class="bc-role" data-i18n="contactRole">Sales Manager</div>', 'Sales Manager'),
 (C, 'contactHoursTitle', '<h3>Working Hours</h3>', '<h3 data-i18n="contactHoursTitle">Working Hours</h3>', 'Working Hours'),
 (C, 'contactSchD1', '<li><span>Monday – Friday</span><span>8:30 – 18:00</span></li>', '<li><span data-i18n="contactSchD1">Monday \u2013 Friday</span><span data-i18n="contactSchT1">8:30 \u2013 18:00</span></li>', 'Monday \u2013 Friday'),
 (C, 'contactSchT1', None, None, '8:30 \u2013 18:00'),
 (C, 'contactSchD2', '<li><span>Saturday</span><span>9:00 – 17:00</span></li>', '<li><span data-i18n="contactSchD2">Saturday</span><span data-i18n="contactSchT2">9:00 \u2013 17:00</span></li>', 'Saturday'),
 (C, 'contactSchT2', None, None, '9:00 \u2013 17:00'),
 (C, 'contactSchD3', '<li><span>Sunday</span><span>By appointment</span></li>', '<li><span data-i18n="contactSchD3">Sunday</span><span data-i18n="contactSchT3">By appointment</span></li>', 'Sunday'),
 (C, 'contactSchT3', None, None, 'By appointment'),
 (C, 'contactSchD4', '<li><span>Online Service</span><span>24 / 7</span></li>', '<li><span data-i18n="contactSchD4">Online Service</span><span data-i18n="contactSchT4">24 / 7</span></li>', 'Online Service'),
 (C, 'contactSchT4', None, None, '24 / 7'),
 (C, 'contactDirectTitle', '<h4>Get In Touch Directly</h4>', '<h4 data-i18n="contactDirectTitle">Get In Touch Directly</h4>', 'Get In Touch Directly'),
 (C, 'contactAddr2', '<p><strong>\U0001F3E2 Address:</strong> Economic and Technological Development Zone, Liaocheng, Shandong Province</p>', '<p data-i18n="contactAddr2">\U0001F3E2 Address: Economic and Technological Development Zone, Liaocheng, Shandong Province</p>', '\U0001F3E2 Address: Economic and Technological Development Zone, Liaocheng, Shandong Province'),
 (C, 'contactFormTitle', '<h3>Send Us A Message</h3>', '<h3 data-i18n="contactFormTitle">Send Us A Message</h3>', 'Send Us A Message'),
 (C, 'contactFormSub', '<p>Fill out the form below and our sales team will get back to you within 24 hours.</p>', '<p data-i18n="contactFormSub">Fill out the form below and our sales team will get back to you within 24 hours.</p>', 'Fill out the form below and our sales team will get back to you within 24 hours.'),
 (C, 'catCarbon', '<option>Carbon Steel</option>', '<option data-i18n="catCarbon">Carbon Steel</option>', 'Carbon Steel'),
 (C, 'catGalvanized', '<option>Galvanized Steel</option>', '<option data-i18n="catGalvanized">Galvanized Steel</option>', 'Galvanized Steel'),
 (C, 'catStainless', '<option>Stainless Steel</option>', '<option data-i18n="catStainless">Stainless Steel</option>', 'Stainless Steel'),
 (C, 'catAluminum', '<option>Aluminum</option>', '<option data-i18n="catAluminum">Aluminum</option>', 'Aluminum'),
 (C, 'catCorrugated', '<option>Corrugated Board</option>', '<option data-i18n="catCorrugated">Corrugated Board</option>', 'Corrugated Board'),
 (C, 'contactOptOther', '<option>Other / Multiple Products</option>', '<option data-i18n="contactOptOther">Other / Multiple Products</option>', 'Other / Multiple Products'),
 (C, 'contactFooterAddr', '<p>\U0001F4CD Shandong Province, Liaocheng, Economic and Technological Development Zone</p>', '<p data-i18n="contactFooterAddr">\U0001F4CD Shandong Province, Liaocheng, Economic and Technological Development Zone</p>', '\U0001F4CD Shandong Province, Liaocheng, Economic and Technological Development Zone'),
]

# ---------------- index.html ----------------
I = 'index.html'
E += [
 (I, 'indexAdv1', '<li>\u2713 High quality products meeting GB/ASTM/JIS/DIN/EN standards</li>', '<li data-i18n="indexAdv1">\u2713 High quality products meeting GB/ASTM/JIS/DIN/EN standards</li>', '\u2713 High quality products meeting GB/ASTM/JIS/DIN/EN standards'),
 (I, 'indexAdv2', '<li>\u2713 Complete specifications available for all product categories</li>', '<li data-i18n="indexAdv2">\u2713 Complete specifications available for all product categories</li>', '\u2713 Complete specifications available for all product categories'),
 (I, 'indexAdv3', '<li>\u2713 Reliable after-sales service and 24/7 online support</li>', '<li data-i18n="indexAdv3">\u2713 Reliable after-sales service and 24/7 online support</li>', '\u2713 Reliable after-sales service and 24/7 online support'),
 (I, 'indexAdv4', '<li>\u2713 More than 20 years trading and manufacture experience</li>', '<li data-i18n="indexAdv4">\u2713 More than 20 years trading and manufacture experience</li>', '\u2713 More than 20 years trading and manufacture experience'),
 (I, 'indexAdv5', '<li>\u2713 Third party inspection (SGS, BV, TUV) is acceptable</li>', '<li data-i18n="indexAdv5">\u2713 Third party inspection (SGS, BV, TUV) is acceptable</li>', '\u2713 Third party inspection (SGS, BV, TUV) is acceptable'),
 (I, 'navHome', '<li><a href="index.html">Home</a></li>', '<li><a href="index.html" data-i18n="navHome">Home</a></li>', 'Home'),
 (I, 'navAbout', '<li><a href="about.html">About Us</a></li>', '<li><a href="about.html" data-i18n="navAbout">About Us</a></li>', 'About Us'),
 (I, 'navProducts', '<li><a href="index.html#products">Products</a></li>', '<li><a href="index.html#products" data-i18n="navProducts">Products</a></li>', 'Products'),
 (I, 'navNews', '<li><a href="news.html">News</a></li>', '<li><a href="news.html" data-i18n="navNews">News</a></li>', 'News'),
 (I, 'navContact', '<li><a href="contact.html">Contact Us</a></li>', '<li><a href="contact.html" data-i18n="navContact">Contact Us</a></li>', 'Contact Us'),
 (I, 'catCarbon', '<li><a href="index.html#products">Carbon Steel</a></li>', '<li><a href="index.html#products" data-i18n="catCarbon">Carbon Steel</a></li>', 'Carbon Steel'),
 (I, 'catGalvanized', '<li><a href="index.html#products">Galvanized Steel</a></li>', '<li><a href="index.html#products" data-i18n="catGalvanized">Galvanized Steel</a></li>', 'Galvanized Steel'),
 (I, 'catStainless', '<li><a href="index.html#products">Stainless Steel</a></li>', '<li><a href="index.html#products" data-i18n="catStainless">Stainless Steel</a></li>', 'Stainless Steel'),
 (I, 'catAluminum', '<li><a href="index.html#products">Aluminum</a></li>', '<li><a href="index.html#products" data-i18n="catAluminum">Aluminum</a></li>', 'Aluminum'),
 (I, 'catCorrugated', '<li><a href="index.html#products">Corrugated Board</a></li>', '<li><a href="index.html#products" data-i18n="catCorrugated">Corrugated Board</a></li>', 'Corrugated Board'),
]

# ---------------- news.html ----------------
N = 'news.html'
E += [
 (N, 'newsBannerTitle', '<h1>Article & News</h1>', '<h1 data-i18n="newsBannerTitle">Article & News</h1>', 'Article & News'),
 (N, 'newsLatestTitle', '<h2>Latest News & Blog</h2>', '<h2 data-i18n="newsLatestTitle">Latest News & Blog</h2>', 'Latest News & Blog'),
 (N, 'newsLatestSub', '<p>Stay updated with the latest from Shandong Stark Steel</p>', '<p data-i18n="newsLatestSub">Stay updated with the latest from Shandong Stark Steel</p>', 'Stay updated with the latest from Shandong Stark Steel'),
 (N, 'newsT1', '<h2><a href="#news-stainless">Stainless Steel: Corrosion-Resistant and Durable Material for High-Demand Scenarios</a></h2>', '<h2><a href="#news-stainless" data-i18n="newsT1">Stainless Steel: Corrosion-Resistant and Durable Material for High-Demand Scenarios</a></h2>', 'Stainless Steel: Corrosion-Resistant and Durable Material for High-Demand Scenarios'),
 (N, 'newsE1', '<p class="news-excerpt">Stainless steel is a high-performance alloy steel primarily composed of iron, chromium (with a minimum content of 10.5%), and nickel, with the addition of elements such as molybdenum in some grades. Its most prominent feature is excellent corrosion resistance, thanks to the dense chromium oxide passive film formed on the surface, which can effectively isolate the metal from the external environment and prevent rust and corrosion...</p>', '<p class="news-excerpt" data-i18n="newsE1">Stainless steel is a high-performance alloy steel primarily composed of iron, chromium (with a minimum content of 10.5%), and nickel, with the addition of elements such as molybdenum in some grades. Its most prominent feature is excellent corrosion resistance, thanks to the dense chromium oxide passive film formed on the surface, which can effectively isolate the metal from the external environment and prevent rust and corrosion...</p>', 'Stainless steel is a high-performance alloy steel primarily composed of iron, chromium (with a minimum content of 10.5%), and nickel, with the addition of elements such as molybdenum in some grades. Its most prominent feature is excellent corrosion resistance, thanks to the dense chromium oxide passive film formed on the surface, which can effectively isolate the metal from the external environment and prevent rust and corrosion...'),
 (N, 'newsT2', '<h2><a href="#news-galvanized">Galvanized Steel: Long-Lasting Corrosion Protection for Industrial Applications</a></h2>', '<h2><a href="#news-galvanized" data-i18n="newsT2">Galvanized Steel: Long-Lasting Corrosion Protection for Industrial Applications</a></h2>', 'Galvanized Steel: Long-Lasting Corrosion Protection for Industrial Applications'),
 (N, 'newsE2', '<p class="news-excerpt">Galvanized steel is a specialized steel product that combines the strength and formability of steel with the excellent corrosion resistance of a zinc coating. By applying a protective zinc layer to the surface of steel, galvanization effectively prevents rust and corrosion, significantly extending the service life of steel products and reducing maintenance costs, making it a preferred material in harsh environments and long-term use scenarios...</p>', '<p class="news-excerpt" data-i18n="newsE2">Galvanized steel is a specialized steel product that combines the strength and formability of steel with the excellent corrosion resistance of a zinc coating. By applying a protective zinc layer to the surface of steel, galvanization effectively prevents rust and corrosion, significantly extending the service life of steel products and reducing maintenance costs, making it a preferred material in harsh environments and long-term use scenarios...</p>', 'Galvanized steel is a specialized steel product that combines the strength and formability of steel with the excellent corrosion resistance of a zinc coating. By applying a protective zinc layer to the surface of steel, galvanization effectively prevents rust and corrosion, significantly extending the service life of steel products and reducing maintenance costs, making it a preferred material in harsh environments and long-term use scenarios...'),
 (N, 'newsT3', '<h2><a href="#news-carbon">Carbon Steel: The Backbone of Modern Industry</a></h2>', '<h2><a href="#news-carbon" data-i18n="newsT3">Carbon Steel: The Backbone of Modern Industry</a></h2>', 'Carbon Steel: The Backbone of Modern Industry'),
 (N, 'newsE3', '<p class="news-excerpt">Carbon steel, also known as non-alloy steel in Europe, is one of the most widely used metal materials globally, playing an irreplaceable role in modern industry, construction, and daily life. Composed primarily of iron and carbon (with a carbon content ranging from 0.05% to 2.1% by weight), it is defined by its simplicity in composition, excellent mechanical properties, and cost-effectiveness, making it the "backbone" of various industrial sectors...</p>', '<p class="news-excerpt" data-i18n="newsE3">Carbon steel, also known as non-alloy steel in Europe, is one of the most widely used metal materials globally, playing an irreplaceable role in modern industry, construction, and daily life. Composed primarily of iron and carbon (with a carbon content ranging from 0.05% to 2.1% by weight), it is defined by its simplicity in composition, excellent mechanical properties, and cost-effectiveness, making it the "backbone" of various industrial sectors...</p>', 'Carbon steel, also known as non-alloy steel in Europe, is one of the most widely used metal materials globally, playing an irreplaceable role in modern industry, construction, and daily life. Composed primarily of iron and carbon (with a carbon content ranging from 0.05% to 2.1% by weight), it is defined by its simplicity in composition, excellent mechanical properties, and cost-effectiveness, making it the "backbone" of various industrial sectors...'),
]

# Execute replacements
errors = []
collected = {}
files_changed = {}
for (fn, key, old, new, en) in E:
    if old is None:  # placeholder key (schedule times) -> only collect
        collected[key] = en
        continue
    path = os.path.join(ROOT, fn)
    html = open(path, encoding='utf-8').read()
    if old not in html:
        errors.append(f'NOT FOUND in {fn}: {key} -> {old[:60]}')
        continue
    cnt = html.count(old)
    if cnt != 1:
        errors.append(f'AMBIGUOUS ({cnt}) in {fn}: {key}')
        continue
    html = html.replace(old, new, 1)
    open(path, 'w', encoding='utf-8').write(html)
    files_changed[fn] = files_changed.get(fn, 0) + 1
    collected[key] = en

if errors:
    print('ERRORS:')
    for e in errors:
        print('  ', e)
else:
    print('All replacements OK.')
print('Files changed:', files_changed)
print('Keys collected:', len(collected))
json.dump(collected, open(os.path.join(ROOT, '.cache_pages_keys.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('Wrote .cache_pages_keys.json')
