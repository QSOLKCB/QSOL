/*
 * QSOL Example Module: Line Counter (C version)
 * A minimal, fast, and transparent line counting utility.
 */

#include <stdio.h>
#include <stdlib.h>

/* Count lines in a file stream */
long count_lines(FILE *fp) {
    long count = 0;
    int ch;
    int last_was_newline = 1;
    
    while ((ch = fgetc(fp)) != EOF) {
        if (ch == '\n') {
            count++;
            last_was_newline = 1;
        } else {
            last_was_newline = 0;
        }
    }
    
    /* Count last line if file doesn't end with newline */
    if (!last_was_newline) {
        count++;
    }
    
    return count;
}

/* Process a single file */
int process_file(const char *filename, long *total) {
    FILE *fp = fopen(filename, "r");
    if (!fp) {
        fprintf(stderr, "Error: Cannot open '%s'\n", filename);
        return 1;
    }
    
    long count = count_lines(fp);
    printf("%s: %ld lines\n", filename, count);
    *total += count;
    
    fclose(fp);
    return 0;
}

int main(int argc, char *argv[]) {
    long total = 0;
    int errors = 0;
    
    if (argc < 2) {
        /* Read from stdin */
        total = count_lines(stdin);
        printf("%ld lines\n", total);
        return 0;
    }
    
    /* Process each file */
    for (int i = 1; i < argc; i++) {
        if (process_file(argv[i], &total) != 0) {
            errors++;
        }
    }
    
    /* Show total if multiple files */
    if (argc > 2) {
        printf("Total: %ld lines\n", total);
    }
    
    return errors > 0 ? 1 : 0;
}
