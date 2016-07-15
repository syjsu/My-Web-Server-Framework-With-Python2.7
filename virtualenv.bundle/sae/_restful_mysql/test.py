
if __name__ == '__main__':
    from converters import conversions
    conn = connection('w.rdc.sae.sina.com.cn', '1mn0k24nzy', 'jhymi4mz2k52mz2ji313i41h5i5xixxklhxx0j42', port=3307, db='app_shellpy', conv=conversions)
    #conn.query("insert into sessions(globals, unpicklables) values('hellodfdfdf', 'dfdfdfdfdfd')")
    #print conn.insert_id()
    #print conn.info()
    #conn.query("select * from sessions")
    #r = conn.store_result()
    #print r.fetch_row(1, how=1)
    #conn.query("select * from sessions limit 0, 2")
    #r = conn.store_result()
    #print r.fetch_row(3)

    #conn.query("update sessions set globals=''")
    #print conn.affected_rows()
    #conn.query('show tables')
    #print conn.store_result().fetch_row(0)

    print conn.escape(())

