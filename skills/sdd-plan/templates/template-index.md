# Template Index — SDD Design Templates

Quick-reference index for all 22 UI/UX design templates. Agent reads this file
first during template selection scoring, then reads the full template file only
after the user picks one.

## Scoring Guide
Match `brainstorm.md` keywords against each template's `category`, `tags`, and
`best_for` fields. Score +3 for category match, +2 for each tag match, +1 for
partial `best_for` keyword overlap. Present the **top 2-3** templates to the user.

## Shared interactions
Some templates depend on a reusable interaction spec instead of duplicating the
technical detail inline — check each template's `uses_shared_interactions`
frontmatter field and read the referenced file under `_shared/interactions/`
**in addition to** the template file itself.

| Shared interaction | File | Used by |
|---|---|---|
| Hand-Drawn Scene Annotation | `_shared/interactions/hand-drawn-annotation.md` | `restaurant-food` (v2), `scene-doodle-annotation`, `shoppable-lifestyle-scene` |

## Versioning
Templates carry a `version` field. Check a template's `changelog` (frontmatter)
for what changed between versions before reusing an old generated page as-is.

---

| # | ID | Name | Category | Tags | Best For | Transparent Images? |
|---|---|---|---|---|---|---|
| 1 | `product-carousel` | Product Carousel Showcase | product-store | e-commerce, carousel, product, showcase, retail, shop | Cửa hàng bán sản phẩm vật lý cần hero section nổi bật với ảnh sản phẩm tách nền | ✅ |
| 2 | `saas-landing` | SaaS Landing Page | saas | saas, software, landing-page, pricing, features, b2b, dashboard | Landing page cho sản phẩm SaaS/phần mềm với gradient mesh và pricing table | ❌ |
| 3 | `portfolio-creative` | Creative Portfolio | portfolio | portfolio, agency, creative, case-study, freelancer, designer | Portfolio cá nhân hoặc agency sáng tạo, showcase dự án | ❌ |
| 4 | `restaurant-food` **(v2)** | Restaurant & Food | food-beverage | restaurant, food, cafe, tea, coffee, menu, dining, bubble-tea | Nhà hàng, quán café, trà sữa, dịch vụ F&B có menu và gallery ảnh đồ ăn — **v2 thêm section Ambiance Scene Annotation (hand-drawn hover)** | ✅ |
| 5 | `fashion-ecommerce` | Fashion E-Commerce | fashion | fashion, clothing, apparel, lookbook, style, boutique, accessories | Cửa hàng thời trang, lookbook, editorial product display | ✅ |
| 6 | `tech-startup` | Tech / AI Startup | tech-startup | tech, ai, startup, saas, innovation, machine-learning, api | Công ty công nghệ/AI startup, dark theme, futuristic design | ❌ |
| 7 | `real-estate` | Real Estate | real-estate | real-estate, property, housing, apartment, rental, listing | Bất động sản, listing property, virtual tour, booking | ❌ |
| 8 | `education-lms` | Education / LMS | education | education, learning, course, lms, school, training, tutorial | Nền tảng học tập, khóa học online, LMS | ❌ |
| 9 | `healthcare-clinic` | Healthcare & Clinic | healthcare | healthcare, clinic, hospital, doctor, medical, wellness, booking | Phòng khám, bệnh viện, dịch vụ y tế, đặt lịch khám | ❌ |
| 10 | `event-conference` | Event & Conference | event | event, conference, summit, workshop, meetup, festival, ticket | Sự kiện, hội nghị, concert, festival, bán vé | ❌ |
| 11 | `fitness-gym` | Fitness & Gym | fitness | fitness, gym, workout, health, training, sport, exercise | Phòng tập gym, fitness app, chương trình tập luyện | ❌ |
| 12 | `travel-tourism` | Travel & Tourism | travel | travel, tourism, hotel, booking, destination, adventure, vacation | Du lịch, đặt tour, khách sạn, trải nghiệm du lịch | ❌ |
| 13 | `music-streaming` | Music & Entertainment | music-entertainment | music, streaming, audio, podcast, entertainment, artist, album | Nền tảng âm nhạc, streaming, artist portfolio, podcast | ❌ |
| 14 | `crypto-fintech` | Crypto & Fintech | crypto-fintech | crypto, fintech, blockchain, trading, defi, wallet, finance | Sàn giao dịch crypto, ứng dụng tài chính, fintech dashboard | ❌ |
| 15 | `photography-studio` | Photography Studio | photography | photography, studio, gallery, photographer, photo, visual | Studio chụp ảnh, photographer portfolio, photo gallery | ❌ |
| 16 | `automotive` | Automotive | automotive | automotive, car, vehicle, motorcycle, dealership, showroom | Ô tô, xe máy, showroom, car dealership | ✅ |
| 17 | `pet-care` | Pet Care | pet-care | pet, veterinary, animal, dog, cat, pet-shop, grooming | Thú cưng, pet shop, dịch vụ thú y, pet grooming | ✅ |
| 18 | `coworking-space` | Coworking Space | coworking | coworking, office, workspace, rental, community, flex-space | Không gian làm việc chung, cho thuê văn phòng | ❌ |
| 19 | `wedding-planner` | Wedding & Event Planning | wedding-event | wedding, event-planning, bridal, ceremony, celebration | Đám cưới, tổ chức sự kiện, wedding planner | ❌ |
| 20 | `news-magazine` | News & Magazine | news-blog | news, blog, magazine, editorial, article, media, journalism | Trang tin tức, blog, tạp chí online, editorial | ❌ |
| 21 | `scene-doodle-annotation` | Scene Doodle Annotation | lifestyle-scene | doodle, hand-drawn, annotation, hotspot, interactive-scene, bakery, cafe, boutique, interior, storytelling | Bakery/café/boutique/thương hiệu nội thất muốn kể chuyện không gian bằng ảnh thật + hover annotation viết tay thay vì text | ❌ (ảnh scene giữ nguyên) |
| 22 | `shoppable-lifestyle-scene` | Shoppable Lifestyle Scene | shoppable-scene | ecommerce, shop-the-look, lifestyle, hotspot, product-scene, organic, grocery, home-decor, interactive-scene | Cửa hàng thực phẩm hữu cơ/grocery/home-decor — "mua ngay trong khung cảnh" thay vì grid sản phẩm, hover hiện mini product card | ❌ (ảnh scene giữ nguyên, ảnh product card có thể tách nền) |
