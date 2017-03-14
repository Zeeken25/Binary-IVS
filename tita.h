#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>

typedef struct
{
    char name[16];
    char desc[64];
    struct tm time;

} T_data;

typedef struct plan T_plan;
struct plan
{
    T_data data;
    T_plan *next;
};

typedef struct
{
    T_plan *first;

} T_day_list;

typedef struct
{
    T_day_list *plans;
    int num;
    char *name;
} T_day;

void add_plan(T_day day);
void del_plan(T_day day, const char* plan_name);
void init_week(T_day *week);
void print_week(T_day *week);
void det_plan(T_day day, const char* plan_name);
void free_lists(T_day *week);
void rewrite_plan(T_day day, const char* plan_name);
void sort_plans(T_day day);
void closest_plan(struct tm *localtime,T_day *week);
//int count_plans(T_day day);
T_plan plans_cmp(T_plan *plan,T_plan *cmp_plan);
//Funcs for hardmem
void save_to_hard(T_day *week);
void load_data(T_day *week);
void add_pl_hard(T_plan *plan,T_day day);
int load_day(FILE *hard);
void load_plans(T_day *week, FILE *hard);
