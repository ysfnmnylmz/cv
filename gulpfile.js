'use strict';

/** Todo:
 * Add Clean Task with sync.
 * @type {*|Gulp}
 */

const gulp = require('gulp');
const rename = require("gulp-rename");
const minifyCss = require("gulp-minify-css");
const sass = require('gulp-sass');
const concat = require('gulp-concat');
const sourcemaps = require('gulp-sourcemaps');
const clean = require('gulp-clean');
const connect = require('gulp-connect');

const homePath = './static_files/',
    scss = homePath + 'scss/style.scss',
    sourceJs = [
        homePath + 'lib/jquery/dist/jquery.min.js',
        homePath + 'lib/jquery-ui/jquery-ui.min.js',
        homePath + 'lib/bootstrap/dist/js/bootstrap.min.js',
        homePath + 'lib/wow/dist/wow.min.js',
        homePath + 'lib/slick-carousel/slick/slick.min.js',
        homePath + 'lib/typed.js/lib/typed.min.js',
        homePath + 'lib/wow/dist/wow.min.js',
        homePath + 'js/main.js',
    ],
    js = homePath + 'js/',
    css = homePath + 'css/';

gulp.task('clean', function (cb) {
    return gulp.src(homePath + 'css/*')
        .pipe(clean(function () {
            if (cb)
                cb();
        }));
});

gulp.task('sass', function () {
    return gulp.src(scss)
        .pipe(sourcemaps.init())
        .pipe(sass().on('error', sass.logError))
        .pipe(sourcemaps.write())
        .pipe(minifyCss())
        .pipe(rename('style-min.css'))
        .pipe(gulp.dest(css))
        .pipe(connect.reload());
});

gulp.task('scripts', function () {
    return gulp.src(sourceJs)
        .pipe(concat('scripts.js'))
        .pipe(rename('scripts.min.js'))
        .pipe(gulp.dest(js))
        .pipe(connect.reload())
});
gulp.task('copy-fonts', function () {
    return gulp
        .src([homePath + '/lib/font-awesome/fonts/**/*'])
        .pipe(gulp.dest(homePath + '/fonts/'))
});

gulp.task('sass:watch', function () {
    gulp.watch(homePath + 'scss/**/*', ['sass']);
});

gulp.task('js:watch', function () {
    gulp.watch(homePath + 'js/**/**', ['scripts']);
});


gulp.task('production', ['scripts', 'copy-fonts', 'sass']);

gulp.task('build', ['scripts', 'copy-fonts', 'sass'], function () {
    gulp.run(['js:watch', 'sass:watch'])
});

gulp.task('default', ['clean'], function () {
    console.log('Clean Finished');
    gulp.run('build');
});