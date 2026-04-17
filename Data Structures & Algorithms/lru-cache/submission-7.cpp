class LRUCache {
public:
    LRUCache(int capacity) {
        cap = capacity;
    }
    
    int get(int key) {
        if(table.count(key) == 0) return -1;
        usagetrack.erase(table[key].second);
        usagetrack.push_back(key);
        table[key].second= --usagetrack.end();
        return table[key].first;
    }
    
    void put(int key, int value) {
        if(table.count(key)){
            usagetrack.erase(table[key].second);
        }else if(table.size() == cap){
            int temp = usagetrack.front();
            usagetrack.pop_front();
            table.erase(temp);
        }
        usagetrack.push_back(key);
        table[key]= {value,--usagetrack.end()};
    }

private:
    unordered_map<int,pair<int, list<int>::iterator>> table;
    list<int>usagetrack;
    int cap;
};
