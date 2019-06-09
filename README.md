# Memorable
Personal Relationship Manager functioning from a daily diary-style entry format.

write()
    runs check_if_started(get_date())
        if TRUE
            open today.txt
        if FALSE
            parse_today()
            save_today()
            reset_today()
            open today.txt

get_date()
    look up the date
    correct for 4am-3:59am
    return date as string

get_daily_questions()
    look up the daily questions
    return list of strings

check_if_started(get_date())
    look for existing file on current date
    return boolean

save_today()
    format today.txt to fit into main
    append today.txt to main
    return null

reset_today()
    clear the file
    get_date()
    get_daily_questions()
    write date
    write daily questions
    write free space
    return null

parse_today()
    iterate over text
        if @ sign
            process_friend(index of @ sign)
        if * sign
            process_daily questions
    return null

process_friend(index of @ sign)
    copy the block
    name = get_name(index of @ sign)
    if name_exists(name)
        append_to_profile("name", "block")
    else
        initialize_profile("name", "block")

get_name(index of @ sign)
    substrings the @name
    returns name as string

name_exists(name)
    if exists
        return ID
    else
        return FALSE






