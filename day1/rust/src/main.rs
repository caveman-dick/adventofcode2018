use std::fs::File;
use std::io::{BufReader, BufRead};

fn main() {
    let path = "../input.txt";

    let input = File::open(path).expect("Cannot open file");
    let buffered = BufReader::new(input);

    let mut answer: i32 = 0;
    let mut previous_answer: i32 = 0;

    for line in buffered.lines() {
        let line_string = line.expect("Error reading line");
        let operator = get_operator(&line_string);
        let current_value = get_value(line_string);

        if operator == '+' {
            answer += current_value;
        } else {
            answer -= current_value;
        }

        println!("{} {} {} = {}", previous_answer, operator, current_value, answer);
        previous_answer = answer;
    }
}

fn get_operator(line: &str) -> char {
    return line.chars().next().expect("Error getting operator");
}

fn get_value(line: String) -> i32 {
    let value_string : String = line.chars().skip(1).take(line.len() - 1).collect();
    return value_string.parse().expect("Error parsing int");
}

#[test]
fn get_operator_should_return_plus() {
    assert_eq!('+', get_operator("+12212121"));
}

#[test]
fn get_operator_should_return_negative() {
    assert_eq!('-', get_operator("-12212121"));
}

#[test]
fn get_value_should_return_the_value_excluding_the_sign() {
    assert_eq!(1234, get_value("-1234".to_string()));
}




