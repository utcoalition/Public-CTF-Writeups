# Products Manager

100 Points - 431 Solves

```
Come play with our products manager application!

http://challenges.fbctf.com:8087
```

## Solution:

I downloaded the source code, and took a look into an interesting function `validate_secret` in `add.php`. 

```php
function validate_secret($secret) {
  if (strlen($secret) < 10) {
    return false;
  }
  $has_lowercase = false;
  $has_uppercase = false;
  $has_number = false;
  foreach (str_split($secret) as $ch) {
    if (ctype_lower($ch)) {
      $has_lowercase = true;
    } else if (ctype_upper($ch)) {
      $has_uppercase = true;
    } else if (is_numeric($ch)) {
      $has_number = true;
    }
  }
  return $has_lowercase && $has_uppercase && $has_number;
}
```

The secret shall be more than 10 bytes, and must have lowercase, uppercase and a number. Apart from that, there are multiple SQL queries - But they are santized properly by using prepared statements. A usual query looks like this

```php
  check_errors($statement);
  $statement->bind_param("s", $name);
  check_errors($statement->execute());
  $res = $statement->get_result();
```

Although, prepared statements are known to be exploited if a variable name is passed directly into the query rather than `?`. There are instances of previous CTFs with such vulnerability type before. But it was not the case here. 

Looking more into other files, there is a comment section which lets us know what to read

```
/*
INSERT INTO products VALUES('facebook', sha256(....), 'FLAG_HERE');
INSERT INTO products VALUES('messenger', sha256(....), ....);
INSERT INTO products VALUES('instagram', sha256(....), ....);
INSERT INTO products VALUES('whatsapp', sha256(....), ....);
INSERT INTO products VALUES('oculus-rift', sha256(....), ....);
*/
```

The vulnerability here in the duplication validation. Hence, the idea is to pass `facebook` with some spaces appended to it such as resulting in a truncation attack. I have done a research on such attacks around 2014 which you can find in my blogpost as [well](https://aadityapurani.com/2015/09/11/column-truncation-sql-injection/) for more depth into the subject.

`facebook       ` and we choose secret for instance `knapKNAP1234` which satisfies the `validate_secret` check and description which whatever you may want to put and finally we can hover to `/view.php` and put the `facebook` and the secret we choose before and we get

##### Flag: fb{4774ck1n9_5q1_w17h0u7_1nj3c710n_15_4m421n9_:)}
