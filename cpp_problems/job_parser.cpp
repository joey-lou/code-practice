#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <format>
#include <unordered_map>
#include <unordered_set>

using namespace std;

class BadInputException : public runtime_error
{
public:
    BadInputException(const string &message) : runtime_error(message) {}
};

struct jobData
{
    int id;
    int runtime_secs;
    int next_id;

    void check_data()
    {
        // raise if malformatted
        if (id <= 0)
            throw BadInputException("ids must be greater than 0");
        if (next_id < 0)
            throw BadInputException("next ids must be greater than -1");
        if (id == next_id)
            throw BadInputException("id must not equal to next_id");
    }
    bool is_end_job()
    {
        return next_id == 0;
    }

    jobData(int i, int r, int n) : id(i), runtime_secs(r), next_id(n) {}
    jobData(vector<int> raw_data)
    {
        if (raw_data.size() != 3)
            throw BadInputException("ids must be greater than 0");
        id = raw_data[0];
        runtime_secs = raw_data[1];
        next_id = raw_data[2];
    }
};

struct jobSummary
{
    int first_id = -1;
    int last_id = -1;
    int runtime_sum_secs = 0;
    int job_counts = 0;

private:
    int next_id = -1;

public:
    void chain_job(jobData *job)
    {
        if (job->id != next_id && job_counts > 0)
            throw BadInputException("Bad chaining");

        if (job_counts == 0)
            first_id = job->id;

        if (job->is_end_job())
            last_id = job->id;

        next_id = job->next_id;
        runtime_sum_secs += job->runtime_secs;
        job_counts++;
    }

    string convert_secs_to_timestamp(int secs)
    {
        string timestamp;
        int hours = secs / 3600;
        int minutes = (secs % 3600) / 60;
        int remain_secs = secs % 60;
        if (hours < 10)
            timestamp += "0";
        timestamp += to_string(hours) + ":";
        if (minutes < 10)
            timestamp += "0";
        timestamp += to_string(minutes) + ":";
        if (remain_secs < 10)
            timestamp += "0";
        timestamp += to_string(remain_secs);
        return timestamp;
    }

    int get_next_id()
    {
        return next_id;
    }

    void print()
    {
        cout << "-" << endl;
        cout << "First Job Id: " << first_id << endl;
        cout << "Last Job Id: " << last_id << endl;
        cout << "Total time: " << convert_secs_to_timestamp(runtime_sum_secs) << endl;
        cout << "Average time: " << convert_secs_to_timestamp(runtime_sum_secs / job_counts) << endl;
    }

    bool operator<(const jobSummary &other) const
    {
        return runtime_sum_secs < other.runtime_sum_secs;
    }

    jobSummary(jobData *head)
    {
        chain_job(head);
    }
};

unordered_map<int, jobData *> &parse_stdin_csv()
{
    string line;
    static unordered_map<int, jobData *> id_to_job;
    int lino = 0;
    while (getline(cin, line))
    {
        stringstream ss(line);
        if (lino == 0)
        {
            lino++; // need to handle out of order header
            continue;
        }
        vector<int> raw_data;
        for (int num; ss >> num;)
        {
            raw_data.push_back(num);
            if (ss.peek() == ',' || ss.peek() == ' ')
                ss.ignore();
        }
        jobData *jd = new jobData(raw_data);
        jd->check_data();
        if (id_to_job.find(jd->id) != id_to_job.end())
            throw BadInputException("Double edge from single node!");
        id_to_job.insert({jd->id, jd});
        lino++;
    }
    return id_to_job;
};

unordered_set<int> &get_first_ids(unordered_map<int, jobData *> &id_to_job)
{
    static unordered_set<int> first_ids;
    for (auto kv : id_to_job)
        first_ids.insert(kv.first);

    for (auto kv : id_to_job)
        first_ids.erase(kv.second->next_id);
    return first_ids;
}

void check_job_graph(unordered_map<int, jobData *> &id_to_job)
{
    unordered_set<int> seen;
    for (auto kv : id_to_job)
    {
        if (seen.find(kv.first) != seen.end())
            continue;
        unordered_set<int> in_path_ids;
        int curr_id = kv.first;
        while (true)
        {
            if (in_path_ids.find(curr_id) != in_path_ids.end())
                throw BadInputException("Cyclic chaining!");
            if (id_to_job.find(curr_id) == id_to_job.end())
                throw BadInputException("Chaining broke!");

            if (id_to_job[curr_id]->is_end_job())
                break;

            in_path_ids.insert(curr_id);
            seen.insert(curr_id);
            curr_id = id_to_job[curr_id]->next_id;
        }
    }
}

vector<jobSummary *> &get_summaries(unordered_set<int> &first_ids, unordered_map<int, jobData *> &edges)
{
    static vector<jobSummary *> summaries;
    for (int hid : first_ids)
    {
        jobSummary *summary = new jobSummary(edges[hid]);
        while (true)
        {
            int next_id = summary->get_next_id();
            if (next_id == 0)
                break;
            if (edges.find(next_id) == edges.end())
            {
                throw BadInputException("Pointing to non-existent Job ID");
            }
            summary->chain_job(edges[next_id]);
        }
        summaries.push_back(summary);
    }
    return summaries;
}

int main()
{
    // parse inputs into vector of tuples
    try
    {
        unordered_map<int, jobData *> id_to_job = parse_stdin_csv();
        unordered_set<int> first_ids = get_first_ids(id_to_job);
        check_job_graph(id_to_job);
        vector<jobSummary *> summaries = get_summaries(first_ids, id_to_job);

        sort(summaries.rbegin(), summaries.rend(), [](jobSummary *a, jobSummary *b) -> bool
             { return *a < *b; });
        for (auto s : summaries)
        {
            s->print();
        }
    }
    catch (const BadInputException &e)
    {
        std::cout << "Malformed Input: " << e.what() << std::endl;
        return 1;
    }
    return 0;
}