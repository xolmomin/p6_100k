from django.db import connection


def statistic_query(f: str):
    cursor = connection.cursor()
    cursor.execute(f'''select table1.name,
                            sum(case when status = 'Yangi' then table1.count else 0 end)         as "Yangi",
                            sum(case when status = 'Qabul qilindi' then table1.count else 0 end) as "Qabul qilindi",
                            sum(case when status = 'Yetkazilmoqda' then table1.count else 0 end) as "Yetkazilmoqda",
                            sum(case when status = 'Yetqazib berildi' then table1.count else 0 end) as "Yetqazib berildi",
                            sum(case when status = 'Qayta qo`ngiroq' then table1.count else 0 end) as "Qayta qo`ngiroq",
                            sum(case when status = 'Spam' then table1.count else 0 end) as "Spam",
                            sum(case when status = 'Qaytib keldi' then table1.count else 0 end) as "Qaytib keldi",
                            sum(case when status = 'HOLD' then table1.count else 0 end) as "HOLD",
                            sum(case when status = 'Arxivlandi' then table1.count else 0 end) as "Arxivlandi",
                            sum(table1.views) "Tashrif"
                        from (SELECT st.name, a.status, st.views, count(*)
                           FROM apps_stream st
                                    JOIN apps_product ap on ap.id = st.product_id
                                    JOIN apps_order a on ap.id = a.product_id
                            WHERE st.name ilike '{f}%'
                           GROUP BY st.name, st.views, a.status) as table1
                        GROUP BY table1.name
                        ORDER BY table1.name''')
    return cursor.fetchall()