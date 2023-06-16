class custom_dic(dict):
    def longest_key(self):
        keys_len = []
        keys = list(self.keys())
        for k in self:
            if isinstance(k,str):
                keys_len.appand(len(k))
            else:
                keys_len.appand(0)
        max_idx = keys_len.index(max(keys_len))
        return key[max_idx]