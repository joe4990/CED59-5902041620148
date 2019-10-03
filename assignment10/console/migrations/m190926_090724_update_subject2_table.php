<?php

use yii\db\Migration;

/**
 * Class m190926_090724_update_subject2_table
 */
class m190926_090724_update_subject2_table extends Migration
{
    /**
     * {@inheritdoc}
     */
    public function safeUp()
    {
        $this->dropColumn('subject','created_at');
        $this->dropColumn('subject','created_by');
        $this->dropColumn('subject','updatad_at');
        $this->dropColumn('subject','updatad_by');

        $this->addColumn('subject','created_at', $this->integer());
        $this->addColumn('subject','created_by', $this->integer());
        $this->addColumn('subject','updated_at', $this->integer());
        $this->addColumn('subject','updated_by', $this->integer());
    }

    /**
     * {@inheritdoc}
     */
    public function safeDown()
    {
        echo "m190926_090724_update_subject2_table cannot be reverted.\n";

        return false;
    }

    /*
    // Use up()/down() to run migration code without a transaction.
    public function up()
    {

    }

    public function down()
    {
        echo "m190926_090724_update_subject2_table cannot be reverted.\n";

        return false;
    }
    */
}
