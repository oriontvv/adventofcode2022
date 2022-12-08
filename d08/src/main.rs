use std::{
    cmp::max,
    error::Error,
    fs::File,
    io::{BufRead, BufReader},
};

fn main() -> Result<(), Box<dyn Error>> {
    let file = File::open("in.txt")?;
    let lines = BufReader::new(file).lines();
    let mut map = vec![];
    for line in lines {
        let row: Vec<char> = line.unwrap().chars().collect();
        map.push(row);
    }

    println!("total visible: {}", task1(&map));
    println!("max scenic score: {}", task2(&map));

    Ok(())
}

fn task1(map: &Vec<Vec<char>>) -> usize {
    let mut total_visible: usize = 0;
    for (col, row_data) in map.iter().enumerate() {
        for (row, height) in row_data.iter().enumerate() {
            if is_visible(row, col, *height, &map) {
                total_visible += 1;
            }
        }
    }
    total_visible
}

fn is_visible(x: usize, y: usize, height: char, map: &Vec<Vec<char>>) -> bool {
    let h = map.len();
    let w = map[0].len();

    let mut visible = true;
    for _x in 0..x {
        if map[y][_x] >= height {
            visible = false;
            break;
        }
    }
    if visible {
        return true;
    }

    visible = true;
    for _x in (x + 1)..w {
        if map[y][_x] >= height {
            visible = false;
            break;
        }
    }
    if visible {
        return true;
    }

    visible = true;
    for _y in 0..y {
        if map[_y][x] >= height {
            visible = false;
            break;
        }
    }
    if visible {
        return true;
    }

    visible = true;
    for _y in (y + 1)..h {
        if map[_y][x] >= height {
            visible = false;
            break;
        }
    }

    visible
}

fn task2(map: &Vec<Vec<char>>) -> usize {
    let mut max_score: usize = 0;
    for (col, row_data) in map.iter().enumerate() {
        for (row, height) in row_data.iter().enumerate() {
            let score = calc_scenic_score(row, col, *height, &map);
            max_score = max(max_score, score);
        }
    }
    max_score
}

fn calc_scenic_score(x: usize, y: usize, height: char, map: &Vec<Vec<char>>) -> usize {
    let h = map.len();
    let w = map[0].len();

    let mut result_score = 1;

    let mut score = 0;
    for _x in (0..x).rev() {
        score += 1;
        if map[y][_x] >= height {
            break;
        }
    }
    result_score *= score;

    score = 0;
    for _x in (x + 1)..w {
        score += 1;
        if map[y][_x] >= height {
            break;
        }
    }
    result_score *= score;

    score = 0;
    for _y in (0..y).rev() {
        score += 1;
        if map[_y][x] >= height {
            break;
        }
    }
    result_score *= score;

    score = 0;
    for _y in (y + 1)..h {
        score += 1;
        if map[_y][x] >= height {
            break;
        }
    }
    result_score *= score;

    result_score
}

#[cfg(test)]
mod test {
    use super::*;

    #[test]
    fn sample_1() {
        let map = vec![
            vec!['3', '0', '3', '7', '3'],
            vec!['2', '5', '5', '1', '2'],
            vec!['6', '5', '3', '3', '2'],
            vec!['3', '3', '5', '4', '9'],
            vec!['3', '5', '3', '9', '0'],
        ];
        assert!(task1(&map) == 21);
    }

    #[test]
    fn sample_2() {
        let map = vec![
            vec!['3', '0', '3', '7', '3'],
            vec!['2', '5', '5', '1', '2'],
            vec!['6', '5', '3', '3', '2'],
            vec!['3', '3', '5', '4', '9'],
            vec!['3', '5', '3', '9', '0'],
        ];
        assert!(task2(&map) == 8);
    }
}
